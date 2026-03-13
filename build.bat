@echo off
REM AI Observer 构建脚本 - 包含桌面快捷方式创建
REM 使用方式: build.bat

echo ========================================
echo   AI Observer v14.0 Build Script
echo ========================================

REM 设置路径
set GAME_DIR=H:\openclaw-workspace\game
set DIST_DIR=H:\openclaw-workspace\dist

echo.
echo [1/3] Cleaning old builds...
if exist "%DIST_DIR%\AI_Observer.exe" del /q "%DIST_DIR%\AI_Observer.exe"

echo.
echo [2/3] Building with PyInstaller...
pyinstaller "%GAME_DIR%\AI_Observer.spec" --clean

if errorlevel 1 (
    echo Build failed!
    exit /b 1
)

echo.
echo [3/3] Creating desktop shortcut...
python H:\openclaw-workspace\scripts\create_shortcut.py "%DIST_DIR%\AI_Observer.exe" "AI_Observer"

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo   Executable: %DIST_DIR%\AI_Observer.exe
echo   Shortcut:   Desktop\AI_Observer.lnk
echo ========================================

pause
