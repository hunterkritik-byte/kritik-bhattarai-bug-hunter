"""Local JSON storage helpers for Signal Hunt. No network or system execution is performed here."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

DATA_FILES = ("scopes.json", "evidence.json", "reports.json")


def now() -> str:
    """Return an ISO 8601 timestamp in UTC for local record keeping."""
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def ensure_workspace(workspace: Path) -> None:
    """Create a transparent local workspace with empty JSON collections."""
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(exist_ok=True)
    manifest = workspace / "workspace.json"
    if not manifest.exists():
        manifest.write_text(
            json.dumps(
                {
                    "format": "signal-hunt-workspace",
                    "version": 1,
                    "created_at": now(),
                    "safety": "Offline workflow records only. No scanning or exploitation commands are included.",
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    for filename in DATA_FILES:
        path = workspace / filename
        if not path.exists():
            path.write_text("[]\n", encoding="utf-8")


def read_collection(workspace: Path, filename: str) -> list[dict[str, Any]]:
    """Read a workspace collection after creating the workspace if necessary."""
    ensure_workspace(workspace)
    try:
        value = json.loads((workspace / filename).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Unable to read {filename}: invalid JSON.") from exc
    if not isinstance(value, list):
        raise ValueError(f"Unable to read {filename}: expected a list of records.")
    return value


def write_collection(workspace: Path, filename: str, records: list[dict[str, Any]]) -> None:
    """Write a workspace collection in a readable JSON form."""
    ensure_workspace(workspace)
    (workspace / filename).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")


def record_id(prefix: str, records: list[dict[str, Any]]) -> str:
    """Create sequential local IDs such as SC-0001 and EV-0001."""
    return f"{prefix}-{len(records) + 1:04d}"


def normalise_target(target: str) -> str:
    """Normalise a hostname-style target for local scope matching only."""
    return target.strip().lower().removeprefix("https://").removeprefix("http://").split("/")[0]


def target_is_authorized(target: str, scopes: list[dict[str, Any]]) -> bool:
    """Check an evidence target against researcher-supplied scope records.

    This is a record-keeping guardrail, not verification of authorization.
    """
    value = normalise_target(target)
    for scope in scopes:
        allowed = normalise_target(str(scope["target"]))
        if allowed.startswith("*."):
            root = allowed[2:]
            if value == root or value.endswith(f".{root}"):
                return True
        if value == allowed:
            return True
    return False
