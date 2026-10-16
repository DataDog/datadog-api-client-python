"""
List all rule outcomes returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    response = api_instance.list_scorecard_outcomes(
        filter_rule_id="00000000-0000-0000-0000-000000000000",
    )

    print(response)
