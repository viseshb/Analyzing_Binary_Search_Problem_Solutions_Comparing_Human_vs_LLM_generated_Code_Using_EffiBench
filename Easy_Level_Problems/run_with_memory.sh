
calculate_memory_usage() {
    local dat_file=$1
    awk '
    BEGIN {
        prev_time = 0;
        prev_mem_mb = 0;
        mem_time_mb_s = 0;
        max_mem_mb = 0;
    }
    NR > 1 {
        mem_in_mb = $2;
        timestamp = $3;

        if (mem_in_mb > max_mem_mb) {
            max_mem_mb = mem_in_mb;
        }

        if (prev_time > 0) {
            time_interval_s = timestamp - prev_time;
            mem_time_mb_s += (prev_mem_mb + mem_in_mb) / 2 * time_interval_s;
        }

        prev_time = timestamp;
        prev_mem_mb = mem_in_mb;
    }
    END {
        total_time_s = timestamp;
        avg_mem_mb = (total_time_s > 0) ? mem_time_mb_s / total_time_s : 0;
        printf "MEM_TIME_MB_S=%.4f\nAVG_MEM_MB=%.20f\nMAX_MEM_MB=%.4f\n", mem_time_mb_s, avg_mem_mb, max_mem_mb;
    }' "$dat_file"
}

# Input args
completion_file="$1"
completion_dat_file="$2"
max_execution_time="$3"
csv_file="benchmark_results.csv"

file_name=$(basename "$completion_file")

# First run header setup
if [ ! -f "$csv_file" ]; then
    echo "File Name,Execution Time (s),Mem × Time (MB·s),Avg Mem (MB),Max Mem (MB)" > "$csv_file"
fi

echo "🚀 Executing $completion_file"
error_output=$(mktemp)
rm -f "$completion_dat_file"

# Run with memory profiler and capture full output
script_output=$(timeout "$max_execution_time" mprof run --interval 0.001 --output "$completion_dat_file" python "$completion_file" 2> "$error_output")
exit_status=$?

# Print the Python script's full output
echo "$script_output"

# Extract execution time reported by Python
execution_time_s=$(echo "$script_output" | awk -F': ' '/Total execution time for all test cases/ { print $2 }')

echo "⏱️  Execution status: $exit_status"

# Handle both success and "soft failure" (exit 1 but valid output)
if [ "$exit_status" -ne 0 ] && [ ! -f "$completion_dat_file" ]; then
    echo "❌ Execution failed and no .dat file found. Removing any leftover files."
    rm -f "$completion_dat_file"
else
    if [ -f "$completion_dat_file" ]; then
        # Compute memory metrics
        eval $(calculate_memory_usage "$completion_dat_file")

        echo ""
        echo "✅ Performance Metrics for $completion_file:"
        echo "---------------------------------------------"
        echo "🕒 Average Execution Time (Python):    ${execution_time_s}"
        echo "📊 Memory × Time (MB·s):               ${MEM_TIME_MB_S}"
        echo "📈 Average Memory Usage (MB):          ${AVG_MEM_MB}"
        echo "🚀 Maximum Memory Usage (MB):          ${MAX_MEM_MB}"
        echo "---------------------------------------------"
        echo "$file_name,$execution_time_s,$MEM_TIME_MB_S,$AVG_MEM_MB,$MAX_MEM_MB" >> "$csv_file"
    else
        echo "⚠️ Execution completed but no .dat file found for $completion_file."
    fi
fi

# Clean up temp error output
rm -f "$error_output"
