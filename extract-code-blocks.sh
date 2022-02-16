#!/usr/bin/env bash

OUTPUT=${1:-examples}
VERSIONS=${2:-v1,v2}

cd ${0%/*}

VERSIONS=(${VERSIONS//,/ })

for version in "${VERSIONS[@]}"; do
    cp -Rn examples/generated/${version} ${OUTPUT}/
done
