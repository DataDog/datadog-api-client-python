"""
Get all powerpacks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.list_powerpacks(
        page_limit=1000,
    )

    print(response)
