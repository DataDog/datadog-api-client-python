#!/usr/bin/env bash

OUTPUT=${1:-examples}
VERSIONS=${2:-v1,v2}

cd ${0%/*}

VERSIONS=(${VERSIONS//,/ })

for version in "${VERSIONS[@]}"; do
    ls docs/$version/*Api.md| xargs -n1 ./extract-code-blocks.awk -v output="${OUTPUT}/$version"
done
