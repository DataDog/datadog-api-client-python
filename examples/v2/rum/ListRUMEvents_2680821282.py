"""
Get a list of RUM events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    items = api_instance.list_rum_events_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
