"""Signal Hunt command-line interface for offline, authorized research workflow management."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent

from .storage import (
    ensure_workspace,
    normalise_target,
    now,
    read_collection,
    record_id,
    target_is_authorized,
    write_collection,
)


CHECKLIST = (
    "1. Confirm written program authorization and exact target scope.",
    "2. Use a test account and avoid accessing data that is not yours.",
    "3. Keep testing low-impact; do not alter, delete, or exfiltrate data.",
    "4. Save reproducible evidence with timestamps and sanitized notes.",
    "5. Verify impact, remediation context, and program reporting requirements.",
)


def workspace_arg(value: str) -> Path:
    return Path(value).expanduser().resolve()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="signal-hunt",
        description="Offline workflow support for authorized bug bounty research. No scanning or exploitation is provided.",
    )
    parser.add_argument("--workspace", type=workspace_arg, default=Path(".signal-hunt").resolve(), help="Local workspace directory (default: ./.signal-hunt).")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("init", help="Create a local Signal Hunt workspace.")

    scope = commands.add_parser("scope", help="Record researcher-supplied scope information.")
    scope_commands = scope.add_subparsers(dest="scope_command", required=True)
    scope_add = scope_commands.add_parser("add", help="Add an authorized target record.")
    scope_add.add_argument("--program", required=True, help="Program or organization name.")
    scope_add.add_argument("--target", required=True, help="Authorized hostname; use *.example.com only when the program explicitly allows it.")
    scope_add.add_argument("--authorization", required=True, help="Reference to the written scope or program rules.")
    scope_add.add_argument("--notes", required=True, help="Short scope notes or exclusions.")
    scope_commands.add_parser("list", help="List local scope records.")

    evidence = commands.add_parser("evidence", help="Store sanitized local evidence notes.")
    evidence_commands = evidence.add_subparsers(dest="evidence_command", required=True)
    evidence_add = evidence_commands.add_parser("add", help="Add an evidence record after confirming scope.")
    evidence_add.add_argument("--title", required=True, help="Concise observation title.")
    evidence_add.add_argument("--target", required=True, help="Target hostname that matches a recorded scope entry.")
    evidence_add.add_argument("--category", choices=("information-disclosure", "authorization", "configuration", "other"), required=True)
    evidence_add.add_argument("--impact", required=True, help="Researcher-assessed impact. Do not overstate it.")
    evidence_add.add_argument("--notes", required=True, help="Sanitized observation and reproduction notes.")
    evidence_add.add_argument("--authorized", action="store_true", help="Confirm that you have written authorization for this target.")
    evidence_commands.add_parser("list", help="List local evidence records.")

    checklist = commands.add_parser("checklist", help="Show responsible research guardrails.")
    checklist.add_subparsers(dest="checklist_command", required=True).add_parser("show", help="Print the authorization and reporting checklist.")

    report = commands.add_parser("report", help="Create draft Markdown reports from local evidence.")
    report_commands = report.add_subparsers(dest="report_command", required=True)
    report_create = report_commands.add_parser("create", help="Create a report template from an evidence ID.")
    report_create.add_argument("--evidence-id", required=True, help="Local evidence ID, for example EV-0001.")
    report_create.add_argument("--output", type=Path, help="Optional output path. Defaults to the workspace reports directory.")
    report_commands.add_parser("list", help="List report files recorded in the workspace.")

    return parser


def print_records(records: list[dict[str, object]], fields: tuple[str, ...]) -> None:
    if not records:
        print("No records found.")
        return
    for record in records:
        print(" | ".join(str(record.get(field, "")) for field in fields))


def handle_scope(args: argparse.Namespace) -> int:
    if args.scope_command == "add":
        scopes = read_collection(args.workspace, "scopes.json")
        target = normalise_target(args.target)
        if any(scope["target"] == target for scope in scopes):
            print(f"Scope record already exists for {target}.")
            return 1
        record = {
            "id": record_id("SC", scopes),
            "program": args.program.strip(),
            "target": target,
            "authorization": args.authorization.strip(),
            "notes": args.notes.strip(),
            "created_at": now(),
        }
        scopes.append(record)
        write_collection(args.workspace, "scopes.json", scopes)
        print(f"Added {record['id']} for {target}. This stores your scope claim; verify authorization independently.")
        return 0
    print_records(read_collection(args.workspace, "scopes.json"), ("id", "program", "target", "authorization"))
    return 0


def handle_evidence(args: argparse.Namespace) -> int:
    if args.evidence_command == "add":
        if not args.authorized:
            print("Refusing to store a finding without --authorized. Confirm written permission first.")
            return 2
        scopes = read_collection(args.workspace, "scopes.json")
        target = normalise_target(args.target)
        if not target_is_authorized(target, scopes):
            print(f"Target '{target}' does not match a recorded scope. Add scope details first; no record was created.")
            return 2
        evidence = read_collection(args.workspace, "evidence.json")
        record = {
            "id": record_id("EV", evidence),
            "title": args.title.strip(),
            "target": target,
            "category": args.category,
            "impact": args.impact.strip(),
            "notes": args.notes.strip(),
            "created_at": now(),
            "status": "draft",
        }
        evidence.append(record)
        write_collection(args.workspace, "evidence.json", evidence)
        print(f"Added {record['id']} as a draft evidence record. Review impact and remove private data before reporting.")
        return 0
    print_records(read_collection(args.workspace, "evidence.json"), ("id", "target", "category", "title", "status"))
    return 0


def report_markdown(evidence: dict[str, object]) -> str:
    return dedent(
        f"""\
        # {evidence['title']}

        > **Draft only.** Verify scope, authorization, impact, and any reporting-program rules before submission. Do not include credentials, private user data, or unsafe payloads.

        | Field | Detail |
        | --- | --- |
        | Evidence ID | {evidence['id']} |
        | Target | {evidence['target']} |
        | Category | {evidence['category']} |
        | Status | {evidence['status']} |
        | Recorded | {evidence['created_at']} |

        ## Summary

        {evidence['notes']}

        ## Security impact

        {evidence['impact']}

        ## Reproduction steps

        1. Confirm the target remains explicitly in scope.
        2. Use only an authorized test account and sanitized data.
        3. Add the minimum reproducible steps here.

        ## Suggested remediation

        Add the smallest technically appropriate mitigation after validating the behavior with the owner.

        ## Disclosure checklist

        - [ ] Scope and authorization were re-verified.
        - [ ] Evidence contains no private data, credentials, or destructive payloads.
        - [ ] Impact is factual and does not overstate the observation.
        - [ ] Program-specific reporting requirements were reviewed.
        """
    )


def handle_report(args: argparse.Namespace) -> int:
    if args.report_command == "list":
        print_records(read_collection(args.workspace, "reports.json"), ("id", "evidence_id", "path", "created_at"))
        return 0

    evidence = read_collection(args.workspace, "evidence.json")
    item = next((record for record in evidence if record["id"] == args.evidence_id.upper()), None)
    if item is None:
        print(f"No local evidence record with ID {args.evidence_id.upper()}.")
        return 2

    reports = read_collection(args.workspace, "reports.json")
    default_path = args.workspace / "reports" / f"{item['id'].lower()}-report.md"
    output = (args.output or default_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report_markdown(item), encoding="utf-8")
    record = {"id": record_id("RP", reports), "evidence_id": item["id"], "path": str(output), "created_at": now()}
    reports.append(record)
    write_collection(args.workspace, "reports.json", reports)
    print(f"Created draft {record['id']}: {output}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "init":
        ensure_workspace(args.workspace)
        print(f"Initialized Signal Hunt workspace: {args.workspace}")
        print("Offline workflow records only. Confirm authorization before any testing.")
        return 0
    if args.command == "scope":
        return handle_scope(args)
    if args.command == "evidence":
        return handle_evidence(args)
    if args.command == "checklist":
        print("\n".join(CHECKLIST))
        return 0
    if args.command == "report":
        return handle_report(args)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
