"""
Get the list of all Synthetic tests returns "OK - Returns the list of all Synthetic tests." response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    items = api_instance.list_tests_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
