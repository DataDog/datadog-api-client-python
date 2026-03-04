"""
Get maintenance returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "maintenance" in the system
MAINTENANCE_DATA_ID = environ["MAINTENANCE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.get_maintenance(
        page_id=STATUS_PAGE_DATA_ID,
        maintenance_id=MAINTENANCE_DATA_ID,
    )

    print(response)
