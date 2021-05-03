#!/bin/bash

set +e

echo "Send me the length of your file, then just cat the file in after it"

read -r length

case $length in
    ''|*[!0-9]*) echo "Not a number; terminating"; exit 1 ;;
    *) echo "Your file is ${length} bytes" ;;
esac

if [ "${length}" -gt "131072" ]; then
    echo "File too long! Max size is 128KiB."
    exit 1
fi

temp=$(mktemp)
dd of="$temp" bs=1 count="${length}" > "$temp"
gdb --batch -ex "info functions" "$temp"
rm "$temp"
