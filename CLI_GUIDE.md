# Signal Hunt CLI

`signal-hunt` is an **offline-first, non-invasive workflow tool** for authorized bug-bounty research. It helps researchers keep scope notes, sanitized evidence, responsible-testing checklists, and draft report templates in a local workspace. It does not send network traffic, enumerate targets, execute shell commands, exploit vulnerabilities, or handle credentials.

## Install

Signal Hunt requires Python 3.10 or later and uses only the Python standard library.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
```

On Windows PowerShell, activate the virtual environment with `.\.venv\Scripts\Activate.ps1`.

## Safe workflow

| Step | Command | Purpose |
| --- | --- | --- |
| Create records | `signal-hunt init` | Creates a local `.signal-hunt` workspace. |
| Record scope | `signal-hunt scope add ...` | Records a researcher-supplied scope claim and authorization reference. |
| Capture notes | `signal-hunt evidence add ... --authorized` | Stores sanitized, local evidence only after an explicit authorization acknowledgement. |
| Review guardrails | `signal-hunt checklist show` | Prints responsible-testing and reporting reminders. |
| Start a report | `signal-hunt report create --evidence-id EV-0001` | Generates a draft Markdown report that requires human review. |

## Example

First, record the scope that you have independently confirmed with the program owner.

```bash
signal-hunt init
signal-hunt scope add \
  --program "Example VRP" \
  --target "*.example.test" \
  --authorization "https://program.example.test/rules" \
  --notes "Dedicated test account only; no production data."
```

Then add a sanitized observation. `--authorized` is required by the tool as a local reminder; it does not prove scope eligibility.

```bash
signal-hunt evidence add \
  --title "Unexpected public configuration field" \
  --target "app.example.test" \
  --category configuration \
  --impact "Potentially exposes a non-sensitive configuration detail." \
  --notes "Observed with a dedicated test account; no private data accessed." \
  --authorized

signal-hunt report create --evidence-id EV-0001
```

## Data location

The default workspace is `.signal-hunt` in the current directory. Override it with `--workspace /path/to/research-records`. Workspaces contain readable JSON records and Markdown drafts, so protect the directory according to the sensitivity of your notes.

## Command reference

```text
signal-hunt init
signal-hunt scope add|list
signal-hunt evidence add|list
signal-hunt checklist show
signal-hunt report create|list
```

Run `signal-hunt --help` or a subcommand with `--help` to view required options.

## Boundaries

The CLI intentionally does not include reconnaissance, scanning, fuzzing, exploitation, request replay, credential storage, or target discovery. Confirm authorization directly with the relevant owner before testing any system, and use the project [security policy](./SECURITY.md) for reporting concerns about this repository.
