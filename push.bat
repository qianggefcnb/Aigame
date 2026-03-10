@echo off
cd /d H:\openclaw-workspace\game
git add .
git commit -m "Auto update: %date% %time%"
git push origin main
