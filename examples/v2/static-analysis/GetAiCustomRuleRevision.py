"""
Get an AI custom rule revision returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_ai_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_ai_custom_rule_revision(
        ruleset_name="my-ai-ruleset",
        rule_name="my-ai-rule",
        id="revision-abc-123",
    )

    print(response)
