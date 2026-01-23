"""
Show Custom Ruleset returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_custom_ruleset(
        ruleset_name="ruleset_name",
    )

    print(response)
