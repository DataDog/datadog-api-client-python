"""
Show Custom Rule Revision returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_custom_rule_revision(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
        id="id",
    )

    print(response)
