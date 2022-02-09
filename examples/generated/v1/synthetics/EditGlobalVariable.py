import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example"  # str | The ID of the global variable.
    body = SyntheticsGlobalVariable(
        attributes=SyntheticsGlobalVariableAttributes(
            restricted_roles=[
                "restricted_roles_example",
            ],
        ),
        description="Example description",
        name="MY_VARIABLE",
        parse_test_options=SyntheticsGlobalVariableParseTestOptions(
            field="content-type",
            parser=SyntheticsVariableParser(
                type=SyntheticsGlobalVariableParserType("raw"),
                value="value_example",
            ),
            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
        ),
        parse_test_public_id="abc-def-123",
        tags=["team:front","test:workflow-1"],
        value=SyntheticsGlobalVariableValue(
            secure=True,
            value="example-value",
        ),
    )  # SyntheticsGlobalVariable | Details of the global variable to update.

    # example passing only required values which don't have defaults set
    try:
        # Edit a global variable
        api_response = api_instance.edit_global_variable(variable_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->edit_global_variable: %s\n" % e)
