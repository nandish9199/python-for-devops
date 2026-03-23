#!/bin/bash
#set -x
BASE_PATH="workspaces/python-for-devops"
TEXT_FILE="filename.txt"

#cd "$BASE_PATH" || exit 1

for folder in ./*/ ; do
    folder=${folder%/}   # remove trailing slash
    folder=${folder#./}
    # Search matching line in text file
    match=$(grep -w "$folder" "$TEXT_FILE")
    if [ ! -z "$match" ]; then
        if [ ! -d "$match" ]; then
            mv "$folder" "$match"
            echo "Renamed: $folder -> $match"
        else
            echo "Skipped: $match already exists"
        fi
    fi
 done
