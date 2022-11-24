#!/bin/bash

DEFAULT_ERROR_CODES="0"

# First arg is the command
# Second arg is the string of acceptable error codes seperated by space. E.g. "0 1"
pre_commit_wrapper () {
  echo "running pre-commit run --all-files --hook-stage=manual ${1}"

  exec 5>&1
  acceptable_errors=${2:-$DEFAULT_ERROR_CODES}
  out=$(pre-commit run --all-files --hook-stage=manual "${1}" | tee >(cat - >&5))
  exit_code=$( echo "$out" | grep -- "- exit code:"  | cut -d":" -f2 | sed 's/[^0-9]*//g' )

  if [[ -n $exit_code ]]; then
    re="([^0-9]|^)$exit_code([^0-9]|$)"
    if ! grep -qE "$re" <<< "$acceptable_errors" ; then
      echo "pre-commit subcommand failed with error_code: $exit_code. See output above"
      exit "$exit_code";
    fi
  fi

  echo "command 'pre-commit run --all-files --hook-stage=manual ${1}' success"
}

rm -rf ./src/datadog_api_client/v1 ./src/datadog_api_client/v2 src/datadog_api_client/{api_client.py,configuration.py,exceptions.py,model_utils.py,rest.py} examples/*
pre_commit_wrapper generator
pre_commit_wrapper examples
pre_commit_wrapper docs
pre_commit_wrapper ruff
pre_commit_wrapper black
pre_commit_wrapper api-docs
