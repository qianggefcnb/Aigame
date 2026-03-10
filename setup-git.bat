git config --global user.email "ai@openclaw.local"
git config --global user.name "OpenClaw AI"

cd H:\openclaw-workspace\game
git add .
git commit -m "Initial commit: AI Observer Game v1.0"
git branch -M main
git remote add origin git@github.com:qianggefcnb/Aigame.git
git push -u origin main
