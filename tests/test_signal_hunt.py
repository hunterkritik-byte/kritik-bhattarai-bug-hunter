"""Regression tests for the offline Signal Hunt workflow."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from signal_hunt.cli import main


class SignalHuntWorkflowTests(unittest.TestCase):
    def test_authorized_scope_to_draft_report(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            workspace = Path(tempdir) / "research"
            base = ["--workspace", str(workspace)]
            self.assertEqual(main([*base, "init"]), 0)
            self.assertEqual(
                main(
                    [
                        *base,
                        "scope",
                        "add",
                        "--program",
                        "Example VRP",
                        "--target",
                        "*.example.test",
                        "--authorization",
                        "Example VRP rules",
                        "--notes",
                        "Testing permitted only with a dedicated account.",
                    ]
                ),
                0,
            )
            self.assertEqual(
                main(
                    [
                        *base,
                        "evidence",
                        "add",
                        "--title",
                        "Sanitized observation",
                        "--target",
                        "app.example.test",
                        "--category",
                        "configuration",
                        "--impact",
                        "Potentially exposes a non-sensitive configuration detail.",
                        "--notes",
                        "Observed only with the research test account; no private data accessed.",
                        "--authorized",
                    ]
                ),
                0,
            )
            self.assertEqual(main([*base, "report", "create", "--evidence-id", "EV-0001"]), 0)
            self.assertTrue((workspace / "reports" / "ev-0001-report.md").exists())

    def test_evidence_requires_authorization_and_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            workspace = Path(tempdir) / "research"
            base = ["--workspace", str(workspace)]
            self.assertEqual(main([*base, "init"]), 0)
            result = main(
                [
                    *base,
                    "evidence",
                    "add",
                    "--title",
                    "Unverified note",
                    "--target",
                    "outside.example",
                    "--category",
                    "other",
                    "--impact",
                    "Unknown",
                    "--notes",
                    "No action taken.",
                ]
            )
            self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
