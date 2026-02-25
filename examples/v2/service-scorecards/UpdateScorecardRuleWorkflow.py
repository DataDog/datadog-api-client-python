"""
Associate workflow with rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

configuration = Configuration()
configuration.unstable_operations["update_scorecard_rule_workflow"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.update_scorecard_rule_workflow(
        rule_id="rule_id",
        workflow_id="550e8400-e29b-41d4-a716-446655440000",
    )
