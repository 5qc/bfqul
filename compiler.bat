@echo off
start cmd /k "cd src & sass --watch style.scss:../static/style.css"
start cmd /k "cd src & tsc -w"
pause