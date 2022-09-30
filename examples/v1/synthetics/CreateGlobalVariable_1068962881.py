"""
Create a global variable from test returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_global_variable import SyntheticsGlobalVariable
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options import (
    SyntheticsGlobalVariableParseTestOptions,
)
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_type import (
    SyntheticsGlobalVariableParseTestOptionsType,
)
from datadog_api_client.v1.model.synthetics_global_variable_value import SyntheticsGlobalVariableValue

# there is a valid "synthetics_api_test_multi_step" in the system
SYNTHETICS_API_TEST_MULTI_STEP_PUBLIC_ID = environ["SYNTHETICS_API_TEST_MULTI_STEP_PUBLIC_ID"]

body = SyntheticsGlobalVariable(
    description="",
    name="GLOBAL_VARIABLE_PAYLOAD_EXAMPLECREATEAGLOBALVARIABLEFROMTESTRETURNSOKRESPONSE",
    tags=[],
    value=SyntheticsGlobalVariableValue(
        secure=False,
        value="",
    ),
    parse_test_public_id=SYNTHETICS_API_TEST_MULTI_STEP_PUBLIC_ID,
    parse_test_options=SyntheticsGlobalVariableParseTestOptions(
        type=SyntheticsGlobalVariableParseTestOptionsType.LOCAL_VARIABLE,
        local_variable_name="EXTRACTED_VALUE",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_global_variable(body=body)

    print(response)
