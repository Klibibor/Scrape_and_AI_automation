param(
    [Parameter(Mandatory=$true)][string]$ScriptPath,
    [Parameter(ValueFromRemainingArguments=$true)][string[]]$Arguments
)
Write-Host "Running: $ScriptPath" -ForegroundColor Cyan
& "L:\git\Scrape_and_AI-main\venv\Scripts\Activate.ps1"
Set-Location "L:\git\Scrape_and_AI-main"
if ($Arguments) { & $ScriptPath @Arguments } else { & $ScriptPath }
