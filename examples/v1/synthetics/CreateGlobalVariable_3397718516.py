"""
Create a TOTP global variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_global_variable_options import SyntheticsGlobalVariableOptions
from datadog_api_client.v1.model.synthetics_global_variable_request import SyntheticsGlobalVariableRequest
from datadog_api_client.v1.model.synthetics_global_variable_totp_parameters import (
    SyntheticsGlobalVariableTOTPParameters,
)
from datadog_api_client.v1.model.synthetics_global_variable_value import SyntheticsGlobalVariableValue

body = SyntheticsGlobalVariableRequest(
    description="",
    is_totp=True,
    name="GLOBAL_VARIABLE_TOTP_PAYLOAD_EXAMPLESYNTHETIC",
    tags=[],
    value=SyntheticsGlobalVariableValue(
        secure=False,
        value="",
        options=SyntheticsGlobalVariableOptions(
            totp_parameters=SyntheticsGlobalVariableTOTPParameters(
                digits=6,
                refresh_interval=30,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_global_variable(body=body)

    print(response)
