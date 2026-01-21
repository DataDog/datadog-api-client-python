"""
Update component returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_component_request import PatchComponentRequest
from datadog_api_client.v2.model.patch_component_request_data import PatchComponentRequestData
from datadog_api_client.v2.model.patch_component_request_data_attributes import PatchComponentRequestDataAttributes
from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = environ["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = PatchComponentRequest(
    data=PatchComponentRequestData(
        attributes=PatchComponentRequestDataAttributes(
            name="Logs Indexing",
        ),
        id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
        type=StatusPagesComponentGroupType.COMPONENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_component(
        page_id=STATUS_PAGE_DATA_ID, component_id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID, body=body
    )

    print(response)
