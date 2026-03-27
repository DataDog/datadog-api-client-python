"""
Patch a test suite returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.json_patch_operation import JsonPatchOperation
from datadog_api_client.v2.model.json_patch_operation_op import JsonPatchOperationOp
from datadog_api_client.v2.model.suite_json_patch_request import SuiteJsonPatchRequest
from datadog_api_client.v2.model.suite_json_patch_request_data import SuiteJsonPatchRequestData
from datadog_api_client.v2.model.suite_json_patch_request_data_attributes import SuiteJsonPatchRequestDataAttributes
from datadog_api_client.v2.model.suite_json_patch_type import SuiteJsonPatchType

body = SuiteJsonPatchRequest(
    data=SuiteJsonPatchRequestData(
        attributes=SuiteJsonPatchRequestDataAttributes(
            json_patch=[
                JsonPatchOperation(
                    op=JsonPatchOperationOp.ADD,
                    path="/name",
                ),
            ],
        ),
        type=SuiteJsonPatchType.SUITES_JSON_PATCH,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.patch_test_suite(public_id="123-abc-456", body=body)

    print(response)
