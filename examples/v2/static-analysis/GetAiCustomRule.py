"""
Get an AI custom rule returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_ai_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_ai_custom_rule(
        ruleset_name="my-ai-ruleset",
        rule_name="my-ai-rule",
    )

    print(response)
