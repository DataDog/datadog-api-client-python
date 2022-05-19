"""
List IP Ranges returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.ip_ranges_api import IPRangesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPRangesApi(api_client)
    response = api_instance.get_ip_ranges()

    print(response)
