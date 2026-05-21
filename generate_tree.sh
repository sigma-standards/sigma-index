#!/bin/bash

# =====================================================
# SIGMA INDEX TREE GENERATOR
# =====================================================

# 1. Get the root directory name where the script is executed
ROOT_NAME=$(basename "$PWD")

# 2. Define the timestamp (mmss_ddmmyy) and output file name
TIMESTAMP=$(date +"%M%S_%d%m%y")
OUTPUT_FILE="${TIMESTAMP}_${ROOT_NAME}.md"

echo "🧹 Cleaning up old directory maps..."
# Safely removes previous files matching the exact timestamp structure for this root folder
rm -f [0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]_${ROOT_NAME}.md

echo "📁 Mapping directory structure into: ${OUTPUT_FILE}..."

# 3. Initialize the Markdown file layout
{
    echo "# Directory Topology: \`${ROOT_NAME}\`"
    echo "Generated on: \`$(date '+%Y-%m-%d %H:%M:%S')\`"
    echo "---"
    echo ""
    echo "## Tree Hierarchy"
    echo ""
    echo "- 📁 **${ROOT_NAME}** *(Root)*"
} > "$OUTPUT_FILE"

# 4. Cross-platform helper function to extract timestamps (Linux vs macOS)
get_metadata() {
    local target="$1"
    if [ "$(uname)" = "Darwin" ]; then
        # macOS stat syntax
        MOD_TIME=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$target" 2>/dev/null)
        BIRTH_TIME=$(stat -f "%SB" -t "%Y-%m-%d %H:%M:%S" "$target" 2>/dev/null)
    else
        # Linux (GNU) stat syntax
        MOD_TIME=$(stat -c '%y' "$target" 2>/dev/null | cut -d'.' -f1)
        BIRTH_TIME=$(stat -c '%w' "$target" 2>/dev/null | cut -d'.' -f1)
        # Fallback if the Linux filesystem doesn't expose birth/creation time
        if [ "$BIRTH_TIME" = "-" ] || [ -z "$BIRTH_TIME" ]; then
            BIRTH_TIME="N/A (Not supported by FS)"
        fi
    fi
}

# 5. Walk through the entire directory tree (excluding hidden items and the output file itself)
find . -not -path '*/.*' | sort | while read -r item; do
    # Skip the root dot entry and the active markdown output file
    if [ "$item" = "." ] || [ "$item" = "./${OUTPUT_FILE}" ]; then
        continue
    fi

    # Format the path string by stripping the leading './'
    CLEAN_PATH="${item#./}"
    
    # Calculate depth natively using pure Bash string manipulation (counts slashes)
    SLASHES="${CLEAN_PATH//[^\/]}"
    DEPTH="${#SLASHES}"
    
    # Generate 4 spaces of indentation per depth level
    INDENT=$(printf '%*s' $(( (DEPTH + 1) * 4 )) '')

    NAME=$(basename "$item")
    get_metadata "$item"

    # Append to markdown depending on whether it's a directory or file
    if [ -d "$item" ]; then
        echo "${INDENT}- 📁 **${NAME}/** | *Created:* \`${BIRTH_TIME}\` | *Modified:* \`${MOD_TIME}\`" >> "$OUTPUT_FILE"
    elif [ -f "$item" ]; then
        # Extract extension safely
        if [[ "$NAME" == *.* ]]; then
            EXT=".${NAME##*.}"
        else
            EXT="no ext"
        fi
        echo "${INDENT}- 📄 ${NAME} (\`${EXT}\`) | *Created:* \`${BIRTH_TIME}\` | *Modified:* \`${MOD_TIME}\`" >> "$OUTPUT_FILE"
    fi
done

echo "✅ Success! New tree generated at the root."
