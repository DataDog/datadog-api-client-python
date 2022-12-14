"""
Get a cloud configuration rule's details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "cloud_configuration_rule" in the system
CLOUD_CONFIGURATION_RULE_ID = environ["CLOUD_CONFIGURATION_RULE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_rule(
        rule_id=CLOUD_CONFIGURATION_RULE_ID,
    )

    print(response)
