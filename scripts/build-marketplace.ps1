param(
  [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
  $OutputPath = Join-Path $repoRoot "dist\ai-dev-protocol-marketplace"
}

$outputRoot = [System.IO.Path]::GetFullPath($OutputPath)
$pluginOutput = Join-Path $outputRoot "plugins\ai-dev-protocol"
$marketplaceOutput = Join-Path $outputRoot ".agents\plugins"

Write-Host "Building AI Dev Protocol marketplace..."
Write-Host "Source: $repoRoot"
Write-Host "Output: $outputRoot"

if (Test-Path $outputRoot) {
  Remove-Item -LiteralPath $outputRoot -Recurse -Force
}

New-Item -ItemType Directory -Force $pluginOutput | Out-Null
New-Item -ItemType Directory -Force $marketplaceOutput | Out-Null

$itemsToCopy = @(
  ".codex-plugin",
  "skills",
  "adapters",
  "docs",
  "README.md",
  "CHANGELOG.md",
  ".gitattributes",
  ".gitignore"
)

foreach ($item in $itemsToCopy) {
  $source = Join-Path $repoRoot $item
  if (-not (Test-Path $source)) {
    throw "Required item missing: $item"
  }

  $destination = Join-Path $pluginOutput $item
  Copy-Item -LiteralPath $source -Destination $destination -Recurse -Force
}

Copy-Item -LiteralPath (Join-Path $repoRoot "marketplace\.agents\plugins\marketplace.json") `
  -Destination (Join-Path $marketplaceOutput "marketplace.json") `
  -Force

Copy-Item -LiteralPath (Join-Path $repoRoot "marketplace\README.md") `
  -Destination (Join-Path $outputRoot "README.md") `
  -Force

Write-Host ""
Write-Host "Marketplace generated successfully."
Write-Host "Next steps:"
Write-Host "1. Push this folder to a GitHub repository such as langji3/ai-dev-protocol-marketplace."
Write-Host "2. In Codex, add that repository as a plugin marketplace."
Write-Host "3. Install the AI Dev Protocol plugin from the marketplace."

