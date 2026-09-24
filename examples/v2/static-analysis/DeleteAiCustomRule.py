"""
Delete an AI custom rule returns "Successfully deleted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_ai_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.delete_ai_custom_rule(
        ruleset_name="my-ai-ruleset",
        rule_name="my-ai-rule",
    )
