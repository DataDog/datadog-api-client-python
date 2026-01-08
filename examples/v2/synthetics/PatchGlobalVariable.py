"""
Patch a global variable returns "OK" response
"""

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

body = GlobalVariableJsonPatchRequest(
    data=GlobalVariableJsonPatchRequestData(
        attributes=GlobalVariableJsonPatchRequestDataAttributes(
            json_patch=[
                JsonPatchOperation(
                    op=JsonPatchOperationOp.ADD,
                    path="/name",
                ),
            ],
        ),
        type=GlobalVariableJsonPatchType.GLOBAL_VARIABLES_JSON_PATCH,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.patch_global_variable(variable_id="variable_id", body=body)

    print(response)
