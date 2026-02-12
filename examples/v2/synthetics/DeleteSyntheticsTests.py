"""
Synthetics: Bulk delete tests returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.deleted_tests_request_delete import DeletedTestsRequestDelete
from datadog_api_client.v2.model.deleted_tests_request_delete_attributes import DeletedTestsRequestDeleteAttributes
from datadog_api_client.v2.model.deleted_tests_request_delete_request import DeletedTestsRequestDeleteRequest
from datadog_api_client.v2.model.deleted_tests_request_type import DeletedTestsRequestType

body = DeletedTestsRequestDeleteRequest(
    data=DeletedTestsRequestDelete(
        attributes=DeletedTestsRequestDeleteAttributes(
            public_ids=[
                "",
            ],
        ),
        type=DeletedTestsRequestType.DELETE_TESTS_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.delete_synthetics_tests(body=body)

    print(response)
