"""
Synthetics: Bulk delete suites returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.deleted_suites_request_delete import DeletedSuitesRequestDelete
from datadog_api_client.v2.model.deleted_suites_request_delete_attributes import DeletedSuitesRequestDeleteAttributes
from datadog_api_client.v2.model.deleted_suites_request_delete_request import DeletedSuitesRequestDeleteRequest
from datadog_api_client.v2.model.deleted_suites_request_type import DeletedSuitesRequestType

body = DeletedSuitesRequestDeleteRequest(
    data=DeletedSuitesRequestDelete(
        attributes=DeletedSuitesRequestDeleteAttributes(
            public_ids=[
                "",
            ],
        ),
        type=DeletedSuitesRequestType.DELETE_SUITES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.delete_synthetics_suites(body=body)

    print(response)
