#!/bin/bash
#
# fetch_prices.sh — validate and summarize the raw price data.
#
# >>> Partner A owns this script. <<<
#
# In a real project this would call an API and download data. Here it inspects
# the local raw data and produces a daily summary log — so you can run one
# command every morning and know what you've got.
#
# Usage:      ./scripts/fetch_prices.sh
# Success:    prints a summary; writes it to logs/fetch_<date>.log; exit 0
# Failure:    prints an error to stderr; exit 1
#
# When done, the following must all be true:
#   - ./scripts/fetch_prices.sh runs green when data/raw/*.csv exists
#   - It creates logs/fetch_YYYY-MM-DD.log with the same content as the console
#   - It exits with code 1 (and prints to stderr) if data/raw/ is missing or empty

set -euo pipefail

INPUT_DIR="data/raw"

LOG_DIR="logs"

LOG_FILE="$LOG_DIR/fetch_$(date +%F).log"

mkdir -p "$LOG_DIR"

if [ ! -d "$INPUT_DIR" ]; then
    echo "ERROR: $INPUT_DIR does not exist" >&2
    exit 1
fi

shopt -s nullglob
files=("$INPUT_DIR"/*.csv)
if [ ${#files[@]} -eq 0 ]; then
    echo "ERROR: no .csv files found in $INPUT_DIR" >&2
    exit 1
fi

{
    echo "fetch_prices — $(date +%F)"
    echo "input: $INPUT_DIR"
    count=0
    for f in "$INPUT_DIR"/*.csv; do
        ticker=$(basename "$f" .csv)
        rows=$(( $(wc -l < "$f") - 1 ))
        echo "  $ticker: $rows rows"
        count=$((count + 1))
    done
    echo "total: $count files"
} | tee "$LOG_FILE"
