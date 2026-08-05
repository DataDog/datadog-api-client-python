Running tests
=============

The Datadog Python API client is mostly using BDD tests to verify its behavior.
They are using recodings to store HTTP interactions, allowing to run the tests without
talking to the API. We also store the test time to be able to freeze.

You can control the behavior with the `RECORD` environment variable:
 - `RECORD=false`, the default value, means replaying HTTP requests from recordings.
 - `RECORD=true` creates or updates recordings. This will need valid credentials in `DD_TEST_CLIENT_API_KEY`
    and `DD_TEST_CLIENT_APP_KEY`.
 - `RECORD=none` ignores recordings. This will also runs tests that we call `integration-only`, i.e.
    tests that we don't record for security reasons. It also needs valid credentials.

Recording and freeze files are stored in the directory `tests/$VERSION/cassettes/test_scenarios/`

To run the tests, it's generally better to use a virtual environment. [tox](https://tox.wiki/) makes it easier to manage them.
For example to run the tests for Python 3.9:

```shell
tox -epy39
```

Generated BDD artifacts
-----------------------

The OpenAPI transformer can generate a shared request-plan database, recording
server, and copy of the feature corpus. After generating those artifacts into
`tests/generated`, run them through the Python SDK's native pytest-bdd adapter:

```shell
./run-bdd-tests.sh
```

Set `BDD_TEST_ARTIFACTS` when the generated artifact directory is elsewhere.
The adapter builds requests from the generated plans and points every SDK client,
including setup and undo calls, at the generated recording server. The SDK does
not need access to the spec repository or the transformer at test runtime.

To pass extra arguments to run the tests, you need to close `tox` arguments with `--`.
You can get more verbose information with the `-v` flag to `pytest`, filter the tests using the `-k` or
specifying the test full path. For example:

```shell
tox -epy39  -- -k test_get_a_list_of_all_incident_teams_returns_ok_response -vvv
```

`-k` takes a regular expression, so you don't have to specify the whole exact
string. See https://docs.pytest.org/ for more information.

The first time you run a test that needs recordings, it will fail with:
`Time file '$PATH/tests/$VERSION/cassettes/test_scenarios/$TEST_NAME.frozen' not found: create one setting 'RECORD=true' or ignore it using 'RECORD=none'`.
