"""
Update status page returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_status_page_request import PatchStatusPageRequest
from datadog_api_client.v2.model.patch_status_page_request_data import PatchStatusPageRequestData
from datadog_api_client.v2.model.patch_status_page_request_data_attributes import PatchStatusPageRequestDataAttributes
from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = PatchStatusPageRequest(
    data=PatchStatusPageRequestData(
        attributes=PatchStatusPageRequestDataAttributes(
            name="A Status Page in US1",
        ),
        id=STATUS_PAGE_DATA_ID,
        type=StatusPageDataType.STATUS_PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_status_page(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
