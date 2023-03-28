"""
Search for incidents returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["search_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    items = api_instance.search_incidents_with_pagination(
        query="state:(active OR stable OR resolved)",
        page_size=2,
    )
    for item in items:
        print(item)
