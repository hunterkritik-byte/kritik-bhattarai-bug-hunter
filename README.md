# Kritik Bhattarai — Bug Hunter Portfolio

> A 3D neon security-research portfolio for **Kritik Bhattarai**, an independent bug bounty hunter from Itahari, Nepal.

The site uses the **Signal After Dark** visual system: a restrained blue-black operations console, Tracer Cyan verification states, a 3D wireframe hero, Nepal field-node metadata, and a small public-information terminal.

## 🚀 Current enhancements

| Area | Updated capability |
| --- | --- |
| Portfolio | Clearer security-research workflow and project discovery |
| Terminal | Safe client-side commands with no shell execution or network access |
| Signal Hunt CLI | Offline scope records, sanitized evidence, checklists, and report scaffolding |
| Hunt Sift | Offline artifact analysis, deterministic triage, SARIF/HTML reporting, and case digests |
| WaveForge | Software-only wireless simulation with reproducible headless telemetry |
| Wi-Fi Detector | Passive suspicious-network indicators with explainable multi-signal scoring |
| Accessibility | Responsive layout and reduced-motion support |
| Deployment | Vite static build with Netlify-ready configuration |

## Research toolkit

This portfolio now acts as the front door for a small, safety-first research toolkit:

```text
ARTIFACT → ANALYZE → TRIAGE → CONTROLLED REPRO → ROOT CAUSE → DOCUMENT
    │          │          │             │              │          │
 Hunt Sift  Wi-Fi       local        authorized     WaveForge   reports
            Detector    scoring       testing
```

All tooling is designed around researcher-supplied data, explicit authorization, reproducibility, and minimal sensitive evidence.

## Highlights

| Area | Included experience |
| --- | --- |
| Identity | Custom signal mark, spaced wordmark, favicon, and direct contact route |
| Visual system | Responsive 3D hero, evidence-led panels, topology motifs, and reduced-motion support |
| Terminal | A fixed-command client-side demo with `help`, `whoami`, `focus`, `contact`, and `clear`; it never executes shell commands or network requests |
| Signal Hunt CLI | An offline-first Python toolkit for scope records, sanitized evidence, responsible-testing checklists, and draft report scaffolding |
| Deployment | Vite static build with a Netlify-ready `netlify.toml` configuration |

## Local development

```bash
pnpm install
pnpm dev
```

Run the type check and production build before publishing changes.

```bash
pnpm check
pnpm build
```

The generated static site is written to `dist/public`.

## Signal Hunt CLI

This repository also contains **Signal Hunt**, a Python command-line companion for authorized security-research workflow management. It is local-only by design and does not scan targets, execute payloads, send network requests, or store credentials.

```bash
python3 -m pip install -e .
signal-hunt init
signal-hunt checklist show
```

Read the complete command reference and safe-use boundaries in [`CLI_GUIDE.md`](./CLI_GUIDE.md). Run the CLI tests with `python3 -m unittest discover -s tests -v`.

## Netlify deployment

The repository includes `netlify.toml`.

| Setting | Value |
| --- | --- |
| Build command | `pnpm build` |
| Publish directory | `dist/public` |
| Node version | `22` |

For more detail, see [`NETLIFY_DEPLOYMENT.md`](./NETLIFY_DEPLOYMENT.md).

## Security

Please follow the private reporting guidance in [`SECURITY.md`](./SECURITY.md). Do not open public issues containing security-sensitive information.

## License

This source code is available under the [MIT License](./LICENSE).
