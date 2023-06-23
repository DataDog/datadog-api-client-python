#!/usr/bin/env bash
set -e
echo "Ensuring all dependencies are present in LICENSE-3rdparty.csv ..."
ALL_DEPS="" # TODO
DEPS_NOT_FOUND=""
for one_dep in $ALL_DEPS; do
    set +e
    if grep "$one_dep" LICENSE-3rdparty.csv > /dev/null 2>&1; then
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

# Explicitly install so we have the scm version.py file available
python -m pip install -e .

python -m mypy src

# Run tests
set +e
python -m pytest -vvv
RESULT=$?
if [ "$RERECORD_FAILED_TESTS" == "true" ] && [ "$RESULT" -ne "0" ]; then
    RECORD=true python -m pytest -vvv --last-failed
    RESULT=$?
fi

exit $RESULT
