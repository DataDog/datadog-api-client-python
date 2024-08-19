"""
Create a FIDO global variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_global_variable_request import SyntheticsGlobalVariableRequest

body = SyntheticsGlobalVariableRequest(
    description="",
    is_fido=True,
    name="GLOBAL_VARIABLE_FIDO_PAYLOAD_EXAMPLESYNTHETIC",
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_global_variable(body=body)

    print(response)
