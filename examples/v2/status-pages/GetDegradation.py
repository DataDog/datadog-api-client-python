"""
Get degradation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = environ["DEGRADATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.get_degradation(
        page_id=STATUS_PAGE_DATA_ID,
        degradation_id=DEGRADATION_DATA_ID,
    )

    print(response)
