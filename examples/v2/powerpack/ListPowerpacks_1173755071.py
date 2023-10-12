"""
Get all powerpacks returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    items = api_instance.list_powerpacks_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
