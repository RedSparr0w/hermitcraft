@echo off
python main.py
echo Close the window now if you do not want to push to GitHub. Press enter to push anyway.
pause >nul
git status
git add --all
git commit -v
git push -u origin master
pause
