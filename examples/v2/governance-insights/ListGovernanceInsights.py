"""
List governance insights returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_insights_api import GovernanceInsightsApi

configuration = Configuration()
configuration.unstable_operations["list_governance_insights"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceInsightsApi(api_client)
    response = api_instance.list_governance_insights()

    print(response)
