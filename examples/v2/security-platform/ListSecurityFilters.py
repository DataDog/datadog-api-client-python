"""
Get all security filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_platform_api import SecurityPlatformApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityPlatformApi(api_client)
    response = api_instance.list_security_filters()

    print(response)
