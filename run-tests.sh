#!/usr/bin/env sh
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
python -m pip install -e .[tests]
# FIXME
pip install -U git+https://github.com/DataDog/dd-trace-py.git@jirikuncar/httplib/distributed-tracing || pip install --find-links=https://s3.amazonaws.com/pypi.datadoghq.com/trace-dev/index.html --pre ddtrace
# Run tests
python -m pytest
