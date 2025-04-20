#!/bin/bash

# === Configuration ===
BASE_DIR="."
MAX_TIME=10

echo "📊 Starting benchmark for all Python files in $BASE_DIR"
echo "⏱️  Max time per script: ${MAX_TIME}s"
echo "==============================================="

# Loop through all Easy_* folders
for folder in "$BASE_DIR"/Easy_*; do
    [ -d "$folder" ] || continue
    folder_name=$(basename "$folder")

    echo ""
    echo "📂 Entering $folder_name"
    echo "-----------------------------------------------"

    # Loop through each Python file in the folder
    for py_file in "$folder"/*.py; do
        [ -f "$py_file" ] || continue
        file_name=$(basename "$py_file")
        dat_file="$folder/${file_name%.py}.dat"

        echo ""
        echo "▶️  Benchmarking: $file_name"
        ./run_with_memory.sh "$py_file" "$dat_file" "$MAX_TIME"
    done
done

echo ""
echo "✅ All benchmarks finished!"
