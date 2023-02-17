"""
Get IP Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ip_allowlist_api import IPAllowlistApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPAllowlistApi(api_client)
    response = api_instance.get_ip_allowlist()

    print(response)
