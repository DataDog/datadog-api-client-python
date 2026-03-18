"""
List all rule outcomes returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    items = api_instance.list_scorecard_outcomes_with_pagination()
    for item in items:
        print(item)
