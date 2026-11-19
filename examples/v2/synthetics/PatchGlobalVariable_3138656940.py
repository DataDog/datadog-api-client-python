"""
Patch a persistent email global variable preserves its address and type
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.global_variable_json_patch_request import GlobalVariableJsonPatchRequest
from datadog_api_client.v2.model.global_variable_json_patch_request_data import GlobalVariableJsonPatchRequestData
from datadog_api_client.v2.model.global_variable_json_patch_request_data_attributes import (
    GlobalVariableJsonPatchRequestDataAttributes,
)
from datadog_api_client.v2.model.global_variable_json_patch_type import GlobalVariableJsonPatchType
from datadog_api_client.v2.model.json_patch_operation import JsonPatchOperation
from datadog_api_client.v2.model.json_patch_operation_op import JsonPatchOperationOp

# there is a valid "synthetics_email_global_variable" in the system
SYNTHETICS_EMAIL_GLOBAL_VARIABLE_ID = environ["SYNTHETICS_EMAIL_GLOBAL_VARIABLE_ID"]

body = GlobalVariableJsonPatchRequest(
    data=GlobalVariableJsonPatchRequestData(
        type=GlobalVariableJsonPatchType.GLOBAL_VARIABLES_JSON_PATCH,
        attributes=GlobalVariableJsonPatchRequestDataAttributes(
            json_patch=[
                JsonPatchOperation(
                    op=JsonPatchOperationOp.REPLACE,
                    path="/description",
                    value="Updated persistent email variable",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.patch_global_variable(variable_id=SYNTHETICS_EMAIL_GLOBAL_VARIABLE_ID, body=body)

    print(response)
