"""
Publish status page returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "unpublished_status_page" in the system
UNPUBLISHED_STATUS_PAGE_DATA_ID = environ["UNPUBLISHED_STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.publish_status_page(
        page_id=UNPUBLISHED_STATUS_PAGE_DATA_ID,
    )
