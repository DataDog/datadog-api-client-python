"""
Create a global variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_global_variable import SyntheticsGlobalVariable
from datadog_api_client.v1.model.synthetics_global_variable_attributes import SyntheticsGlobalVariableAttributes
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options import (
    SyntheticsGlobalVariableParseTestOptions,
)
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_type import (
    SyntheticsGlobalVariableParseTestOptionsType,
)
from datadog_api_client.v1.model.synthetics_global_variable_parser_type import SyntheticsGlobalVariableParserType
from datadog_api_client.v1.model.synthetics_global_variable_value import SyntheticsGlobalVariableValue
from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles
from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser

body = SyntheticsGlobalVariable(
    attributes=SyntheticsGlobalVariableAttributes(
        restricted_roles=SyntheticsRestrictedRoles(
            [
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            ]
        ),
    ),
    description="Example description",
    name="MY_VARIABLE",
    parse_test_options=SyntheticsGlobalVariableParseTestOptions(
        field="content-type",
        local_variable_name="LOCAL_VARIABLE",
        parser=SyntheticsVariableParser(
            type=SyntheticsGlobalVariableParserType.REGEX,
            value=".*",
        ),
        type=SyntheticsGlobalVariableParseTestOptionsType.HTTP_BODY,
    ),
    parse_test_public_id="abc-def-123",
    tags=[
        "team:front",
        "test:workflow-1",
    ],
    value=SyntheticsGlobalVariableValue(
        secure=True,
        value="value",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_global_variable(body=body)

    print(response)
