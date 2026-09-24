"""
Get all downtimes returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    items = api_instance.list_downtimes_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
