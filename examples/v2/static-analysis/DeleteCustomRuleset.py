"""
Delete Custom Ruleset returns "Successfully deleted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["delete_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.delete_custom_ruleset(
        ruleset_name="ruleset_name",
    )
