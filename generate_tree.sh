#!/usr/bin/env bash

# =====================================================
# SIGMA INDEX TREE GENERATOR
# =====================================================

PROJECT_ROOT="$(pwd)"

TIMESTAMP=$(date +"%M%S_%d%m%Y")
OUTPUT_FILE="${TIMESTAMP}_Tree.md"

# -----------------------------------------------------
# Remove old tree markdown files
# -----------------------------------------------------

find . -maxdepth 1 -type f -name "*_Tree.md" -delete

# -----------------------------------------------------
# Create markdown header
# -----------------------------------------------------

echo "# Sigma Index Project Tree" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "- Generated At: $(date)" >> "$OUTPUT_FILE"
echo "- Project Root: $PROJECT_ROOT" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo '```text' >> "$OUTPUT_FILE"

# -----------------------------------------------------
# Generate tree using find
# -----------------------------------------------------

find . -print0 | sort -z | while IFS= read -r -d '' item
do

    # Skip generated tree files
    if [[ "$item" == ./*_Tree.md ]]; then
        continue
    fi

    depth=$(echo "$item" | awk -F"/" '{print NF-1}')

    indent=""

    for ((i=0; i<depth; i++))
    do
        indent="${indent}│   "
    done

    name=$(basename "$item")

    created=$(stat -c '%w' "$item" 2>/dev/null)
    modified=$(stat -c '%y' "$item" 2>/dev/null)

    [[ "$created" == "-" ]] && created="N/A"

    echo "${indent}├── ${name}" >> "$OUTPUT_FILE"
    echo "${indent}│   [Created : ${created}]" >> "$OUTPUT_FILE"
    echo "${indent}│   [Modified: ${modified}]" >> "$OUTPUT_FILE"

done

# -----------------------------------------------------
# Footer
# -----------------------------------------------------

echo '```' >> "$OUTPUT_FILE"

echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Tree generation completed successfully." >> "$OUTPUT_FILE"

# -----------------------------------------------------
# Final message
# -----------------------------------------------------

echo ""
echo "=================================="
echo "Tree file created:"
echo "$OUTPUT_FILE"
echo "=================================="
echo ""
