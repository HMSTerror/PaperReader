@echo off
setlocal

set "ROOT=%~dp0"
set "NODE_DIR="

for %%D in ("E:\DiT\.tools\node\node-v22.22.1-win-x64" "%ROOT%tools\nodejs" "C:\Program Files\nodejs" "C:\Program Files (x86)\nodejs") do (
  if exist "%%~D\node.exe" (
    set "NODE_DIR=%%~D"
    goto :node_found
  )
)

echo Could not find a usable Node.js installation.
echo Checked:
echo   E:\DiT\.tools\node\node-v22.22.1-win-x64
echo   %ROOT%tools\nodejs
echo   C:\Program Files\nodejs
echo   C:\Program Files ^(x86^)\nodejs
exit /b 1

:node_found
set "PATH=%NODE_DIR%;%PATH%"

echo Using Node.js from: %NODE_DIR%
pushd "%ROOT%"

node --version || goto :failed
echo.
echo Rebuilding paper index...
node scripts\generate-papers-index.mjs || goto :failed
echo.
echo Starting PaperReader at http://127.0.0.1:8000
echo Press Ctrl+C to stop the server.
echo.
node scripts\serve-static.mjs 8000
set "EXIT_CODE=%ERRORLEVEL%"
popd
exit /b %EXIT_CODE%

:failed
set "EXIT_CODE=%ERRORLEVEL%"
popd
exit /b %EXIT_CODE%
