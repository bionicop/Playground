:: This Batch is for copying Windows File Structure without bytes.

@echo off

rem Define the destination directory
set "dst_dir=%~d0\dest"

rem Check if the destination folder exists, if not create it
if not exist "%dst_dir%" (
  md "%dst_dir%"
)

rem Ask the user to choose the drive
set /p drive=Enter the drive letter (e.g. C: ): 

rem Copy the folder structure
ROBOCOPY %drive% %dst_dir% /E /256 /CREATE /R:10 /W:30

rem Remove the traces of the script
del %0