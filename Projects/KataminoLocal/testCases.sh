#!/bin/bash
PYTHON_SCRIPT="katamino.py"
INPUT_FILES=("input1.txt" "input2.txt" "input3.txt" "input4.txt" "input5.txt" "input6.txt" "input7.txt" "input8.txt" "input9.txt" "input10.txt")
for INPUT_FILE in "${INPUT_FILES[@]}"; do
    OUTPUT_FILE="${INPUT_FILE/input/output}"
    START_TIME=$(date +%s)
    python3 "$PYTHON_SCRIPT" < "$INPUT_FILE" > "$OUTPUT_FILE"
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    echo "Procesado $INPUT_FILE -> $OUTPUT_FILE en $DURATION segundos!!!!!!!!!!!!!!"
done

