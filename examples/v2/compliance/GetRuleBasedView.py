"""
Get the rule-based view of compliance findings returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.compliance_api import ComplianceApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_rule_based_view"] = True
with ApiClient(configuration) as api_client:
    api_instance = ComplianceApi(api_client)
    response = api_instance.get_rule_based_view(
        to=1739982278000,
    )

    print(response)
