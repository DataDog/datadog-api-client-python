#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 2
fi

./extract-code-blocks.sh examples $1

ls examples/$1/*/*.pybeta | xargs -P $(($(nproc)*2)) -n 1 python -m py_compile
if [ $? -ne 0 ]; then
    echo -e "Failed to build examples"
    exit 1
fi
