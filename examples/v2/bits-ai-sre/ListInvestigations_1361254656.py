"""
List Bits AI SRE investigations returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_aisre_api import BitsAISREApi

configuration = Configuration()
configuration.unstable_operations["list_investigations"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAISREApi(api_client)
    items = api_instance.list_investigations_with_pagination()
    for item in items:
        print(item)
