"""
Get a security filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_platform_api import SecurityPlatformApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityPlatformApi(api_client)
    response = api_instance.get_security_filter(
        security_filter_id="security_filter_id",
    )

    print(response)
