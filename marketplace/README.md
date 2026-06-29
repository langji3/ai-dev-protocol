# AI Dev Protocol Marketplace

This folder is the source template for a Codex plugin marketplace repository.

Use it to publish AI Dev Protocol as a marketplace instead of asking users to manually create a local marketplace file.

## Generated Repository Shape

Run the build script from the plugin repository:

```powershell
.\scripts\build-marketplace.ps1
```

The script generates:

```text
dist/
  ai-dev-protocol-marketplace/
    README.md
    .agents/
      plugins/
        marketplace.json
    plugins/
      ai-dev-protocol/
        .codex-plugin/
          plugin.json
        skills/
        adapters/
        README.md
        CHANGELOG.md
        docs/
```

Publish `dist/ai-dev-protocol-marketplace` to a separate GitHub repository, for example:

```text
https://github.com/langji3/ai-dev-protocol-marketplace
```

Then users can add that repository as a Codex plugin marketplace and install `ai-dev-protocol`.

## Marketplace Entry

The generated marketplace file points at the plugin source inside the marketplace repository:

```json
{
  "name": "ai-dev-protocol-marketplace",
  "interface": {
    "displayName": "AI Dev Protocol Marketplace"
  },
  "plugins": [
    {
      "name": "ai-dev-protocol",
      "source": {
        "source": "local",
        "path": "./plugins/ai-dev-protocol"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Coding"
    }
  ]
}
```

