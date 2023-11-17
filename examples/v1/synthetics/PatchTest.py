"""
Patch a Synthetic test returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_patch_test_body import SyntheticsPatchTestBody
from datadog_api_client.v1.model.synthetics_patch_test_operation import SyntheticsPatchTestOperation
from datadog_api_client.v1.model.synthetics_patch_test_operation_name import SyntheticsPatchTestOperationName

# there is a valid "synthetics_api_test" in the system
SYNTHETICS_API_TEST_PUBLIC_ID = environ["SYNTHETICS_API_TEST_PUBLIC_ID"]

body = SyntheticsPatchTestBody(
    data=[
        SyntheticsPatchTestOperation(
            op=SyntheticsPatchTestOperationName.REPLACE,
            path="/name",
            value="New test name",
        ),
        SyntheticsPatchTestOperation(
            op=SyntheticsPatchTestOperationName.REMOVE,
            path="/config/assertions/0",
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.patch_test(public_id=SYNTHETICS_API_TEST_PUBLIC_ID, body=body)

    print(response)
