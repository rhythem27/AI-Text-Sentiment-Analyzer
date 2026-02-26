<#
.SYNOPSIS
A script to run the FastAPI backend and Streamlit frontend concurrently.
#>

$ErrorActionPreference = "Stop"

$FastAPIPid = $null
$StreamlitPid = $null

# Define the cleanup function to securely stop background processes
function Invoke-Cleanup {
    Write-Host "Shutting down servers..." -ForegroundColor Yellow
    
    if ($FastAPIPid) {
        Write-Host "Stopping FastAPI backend (PID: $FastAPIPid)..."
        Stop-Process -Id $FastAPIPid -Force -ErrorAction SilentlyContinue
    }
    
    if ($StreamlitPid) {
        Write-Host "Stopping Streamlit frontend (PID: $StreamlitPid)..."
        Stop-Process -Id $StreamlitPid -Force -ErrorAction SilentlyContinue
    }
    
    Write-Host "All processes have been terminated." -ForegroundColor Green
    exit
}

# Attach the termination events directly
[console]::TreatControlCAsInput = $false
# To handle graceful exits on Windows gracefully when pressing CTRL + C:
[System.Console]::CancelKeyPress += {
    $_.Cancel = $true
    Invoke-Cleanup
}

Write-Host "Starting FastAPI backend..." -ForegroundColor Cyan
$fastapiJob = Start-Process -NoNewWindow -PassThru -FilePath "poetry" -ArgumentList "run uvicorn api:app --host 127.0.0.1 --port 8000"
$FastAPIPid = $fastapiJob.Id

Start-Sleep -Seconds 3 # Provide buffering wait state for backend bindings

Write-Host "Starting Streamlit frontend..." -ForegroundColor Cyan
$streamlitJob = Start-Process -NoNewWindow -PassThru -FilePath "poetry" -ArgumentList "run streamlit run app.py --server.port 8501"
$StreamlitPid = $streamlitJob.Id

Write-Host "`nBoth servers are running." -ForegroundColor Green
Write-Host "FastAPI backend: http://localhost:8000"
Write-Host "Streamlit frontend: http://localhost:8501"
Write-Host "Press Ctrl+C to stop both servers.`n" -ForegroundColor Red

# Wait infinitely
try {
    Wait-Process -Id $FastAPIPid, $StreamlitPid
} finally {
    Invoke-Cleanup
}
