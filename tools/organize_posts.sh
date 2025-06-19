#!/bin/bash

POSTS_DIR="/Users/panic/codespace/project_mine/nianqinianyi.github.io/posts"

find "$POSTS_DIR" -type f -name "*.md" | while read -r file; do
    filename=$(basename "$file")
    if [[ $filename =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})-(.*)\.md$ ]]; then
        year="${BASH_REMATCH[1]}"
        month="${BASH_REMATCH[2]}"
        day="${BASH_REMATCH[3]}"
        rest="${BASH_REMATCH[4]}"
        new_dir="$POSTS_DIR/$year/${month}${day}"
        mkdir -p "$new_dir"
        new_path="$new_dir/$rest.md"
        mv "$file" "$new_path"
        echo "Moved $file to $new_path"
    fi
done