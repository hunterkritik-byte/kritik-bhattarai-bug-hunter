# Kritik Bhattarai — Bug Hunter Portfolio

> A 3D neon security-research portfolio for **Kritik Bhattarai**, an independent bug bounty hunter from Itahari, Nepal.

The site uses the **Signal After Dark** visual system: a restrained blue-black operations console, Tracer Cyan verification states, a 3D wireframe hero, Nepal field-node metadata, and a small public-information terminal.

## Highlights

| Area | Included experience |
| --- | --- |
| Identity | Custom signal mark, spaced wordmark, favicon, and direct contact route |
| Visual system | Responsive 3D hero, evidence-led panels, topology motifs, and reduced-motion support |
| Terminal | A fixed-command client-side demo with `help`, `whoami`, `focus`, `contact`, and `clear`; it never executes shell commands or network requests |
| Signal Hunt CLI | An offline-first Python toolkit for scope records, sanitized evidence, responsible-testing checklists, and draft report scaffolding |
| Deployment | Vite static build with a Netlify-ready `netlify.toml` configuration |

## Local development

Install dependencies and start the development server.

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

The repository includes `netlify.toml`. When importing this repository into Netlify, use the following configuration.

| Setting | Value |
| --- | --- |
| Build command | `pnpm build` |
| Publish directory | `dist/public` |
| Node version | `22` |

For more detail, see [`NETLIFY_DEPLOYMENT.md`](./NETLIFY_DEPLOYMENT.md).

## Contact

For responsible security communication or portfolio contact, email [projectvuln@gmail.com](mailto:projectvuln@gmail.com) or visit [github.com/hunterkritik-byte](https://github.com/hunterkritik-byte).

## Security

Please follow the private reporting guidance in [`SECURITY.md`](./SECURITY.md). Do not open public issues containing security-sensitive information.

## License

This source code is available under the [MIT License](./LICENSE).
