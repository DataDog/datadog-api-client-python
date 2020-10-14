#!/usr/bin/env bash
set -e
echo "Ensuring all dependencies are present in LICENSE-3rdparty.csv ..."
ALL_DEPS="" # TODO
DEPS_NOT_FOUND=""
for one_dep in `echo $ALL_DEPS`; do
    set +e
    cat LICENSE-3rdparty.csv | grep "$one_dep" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        DEPS_NOT_FOUND="${DEPS_NOT_FOUND}\n${one_dep}<LICENSE>,<COPYRIGHT>"
    fi
    set -e
done
if [ -n "$DEPS_NOT_FOUND" ]; then
    echo "Some dependencies were not found in LICENSE-3rdparty.csv, please add: $DEPS_NOT_FOUND"
    exit 1
else
    echo "LICENSE-3rdparty.csv is up to date"
fi

# Install test dependencies
python -m pip install -e .
# Run tests
set +e
python -m pytest
RESULT=$?
if [ "$RERECORD_FAILED_TESTS" == "true" -a "$RESULT" -ne 0 ]; then
    RECORD=true python -m pytest --last-failed
    RESULT=$?
fi
exit $RESULT
