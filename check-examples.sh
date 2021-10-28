#!/usr/bin/env bash

./extract-code-blocks.sh examples

ls examples/*/*/*.py | xargs -P $(($(nproc)*2)) -n 1 python -m py_compile
if [ $? -ne 0 ]; then
    echo -e "Failed to build examples"
    exit 1
fi
