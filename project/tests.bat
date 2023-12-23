@echo off

rem Define output file paths
set "output_file_it20=..\data\ball_by_ball_it20.csv"
set "output_file_ipl=..\data\ball_by_ball_ipl.csv"

rem Remove existing output files if they exist
if exist "%output_file_it20%" del "%output_file_it20%"
if exist "%output_file_ipl%" del "%output_file_ipl%"

rem Execute the data pipeline with a message
echo Executing data pipeline...
python pull_data.py

rem Validate the output files
if exist "%output_file_it20%" (
    echo IT20 output file exists: %output_file_it20%
) else (
    echo IT20 output file not found: %output_file_it20%
    exit /b 1
)

if exist "%output_file_ipl%" (
    echo IPL output file exists: %output_file_ipl%
) else (
    echo IPL output file not found: %output_file_ipl%
    exit /b 1
)

echo Tests passed successfully!
