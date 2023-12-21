#!/bin/bash

# Define output file paths
output_file_it20="../data/ball_by_ball_it20.csv"
output_file_ipl="../data/ball_by_ball_ipl.csv"

# Remove existing output files if they exist
rm -f "$output_file_it20"
rm -f "$output_file_ipl"

# Execute the data pipeline in the background with a message
echo "Executing data pipeline..."
python3 pull_data.py &

# Wait for the pipeline to finish and display a message
wait
echo "Data pipeline execution completed."

# Validate the output files
if [ -f "$output_file_it20" ]; then
    echo "IT20 output file exists: $output_file_it20"
else
    echo "IT20 output file not found: $output_file_it20"
    exit 1
fi

if [ -f "$output_file_ipl" ]; then
    echo "IPL output file exists: $output_file_ipl"
else
    echo "IPL output file not found: $output_file_ipl"
    exit 1
fi

echo "Tests passed successfully!"
