"""
List Custom Rule Revisions returns "Successful response" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["list_custom_rule_revisions"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    items = api_instance.list_custom_rule_revisions_with_pagination(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
    )
    for item in items:
        print(item)
