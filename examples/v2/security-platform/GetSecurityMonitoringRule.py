"""
Get a rule's details returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_platform_api import SecurityPlatformApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityPlatformApi(api_client)
    response = api_instance.get_security_monitoring_rule(
        rule_id="rule_id",
    )

    print(response)
