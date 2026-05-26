"""
List AI custom rule revisions returns "Successful response" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["list_ai_custom_rule_revisions"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    items = api_instance.list_ai_custom_rule_revisions_with_pagination(
        ruleset_name="my-ai-ruleset",
        rule_name="my-ai-rule",
    )
    for item in items:
        print(item)
