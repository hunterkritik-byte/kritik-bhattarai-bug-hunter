# Netlify deployment guide

This project is prepared as a **static Vite site**. It contains no platform branding in the visible website and can be deployed to a Netlify account you control.

## Publish from GitHub

Push this project to the GitHub repository connected to your Netlify account. In Netlify, select **Add new project → Import an existing project**, choose the repository, and use the following settings.

| Setting | Value |
| --- | --- |
| Build command | `pnpm build` |
| Publish directory | `dist/public` |
| Node version | `22` |

The included `netlify.toml` already defines these settings and adds a single-page-app fallback route. After Netlify completes the build, use its domain controls to assign a custom domain if you have one.

## Publish from a local folder

Build the site with `pnpm build`. Then, in the Netlify dashboard, use the manual deploy flow and upload the contents of the generated `dist/public` directory. Do not upload the whole repository when using the manual deploy flow.

## Final checks

Open the deployed address on a desktop browser and a phone. Confirm the email link opens `projectvuln@gmail.com`, the GitHub link opens `https://github.com/hunterkritik-byte`, and the site title and icon identify **Kritik Bhattarai — Bug Hunter**.
