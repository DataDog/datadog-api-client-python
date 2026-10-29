"""
Get a rule proposal returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "rule_proposal" in the system
RULE_PROPOSAL_DATA_ID = environ["RULE_PROPOSAL_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_security_monitoring_rule_proposal"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_rule_proposal(
        proposal_id=RULE_PROPOSAL_DATA_ID,
    )

    print(response)
