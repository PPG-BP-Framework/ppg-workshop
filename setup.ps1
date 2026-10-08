param(
    [string]$EnvironmentName = "ppg_workshop_showcase",
    [string]$CondaExecutable = "conda",
    [string]$PythonVersion = "3.11.17"
)
$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot
try {
    $installation = Get-Content -LiteralPath (Join-Path $PSScriptRoot "installation.json") -Raw | ConvertFrom-Json
    & $CondaExecutable create --name $EnvironmentName --override-channels -c conda-forge "python=$PythonVersion" pip git --yes
    if ($LASTEXITCODE -ne 0) { throw "Conda environment creation failed." }
    & $CondaExecutable run --no-capture-output --name $EnvironmentName python -m pip install -r requirements-tested-windows-cpu.txt $installation.pip_requirement
    if ($LASTEXITCODE -ne 0) { throw "Package installation failed." }
    & $CondaExecutable run --no-capture-output --name $EnvironmentName python -m pip check
    if ($LASTEXITCODE -ne 0) { throw "Dependency check failed." }
    & $CondaExecutable run --no-capture-output --name $EnvironmentName python -m ipykernel install --sys-prefix --name ppg-workshop-showcase --display-name "PPG Workshop Showcase"
    if ($LASTEXITCODE -ne 0) { throw "Kernel registration failed." }
    Write-Host "Ready. Run: conda activate $EnvironmentName"
    Write-Host "Then: jupyter lab workshop_cpu_short.ipynb"
} finally { Pop-Location }
