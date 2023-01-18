:: This Batch is for copying Windows File Structure with bytes.

@echo off

rem Define the source and destination directories
set "src_dir=E:\js"
set "dst_dir=%~d0\dest"

rem Copy the folder structure
xcopy /E /I /Y "%src_dir%\" "%dst_dir%"

rem Remove the script from the recent list and the recycle bin
del %0

rem Clear the command history
doskey /history

rem Clear the environment variables
set "src_dir="
set "dst_dir="
set "file_types="