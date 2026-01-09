"""
Delete component returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = environ["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_component(
        page_id=STATUS_PAGE_DATA_ID,
        component_id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
    )
