"""
List Bits AI SRE investigations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_aisre_api import BitsAISREApi

configuration = Configuration()
configuration.unstable_operations["list_investigations"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAISREApi(api_client)
    response = api_instance.list_investigations()

    print(response)
