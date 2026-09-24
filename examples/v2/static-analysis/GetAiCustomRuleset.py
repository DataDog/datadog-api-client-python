"""
Get an AI custom ruleset returns "Successful response" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_ai_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_ai_custom_ruleset(
        ruleset_name="my-ai-ruleset",
    )

    print(response)
