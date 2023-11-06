"""
List all rules returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

configuration = Configuration()
configuration.unstable_operations["list_scorecard_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    items = api_instance.list_scorecard_rules_with_pagination(
        page_size=2,
        filter_rule_custom=True,
        fields_rule="name",
    )
    for item in items:
        print(item)
