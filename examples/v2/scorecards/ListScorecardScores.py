"""
List all scores returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi
from datadog_api_client.v2.model.scorecard_scores_aggregation import ScorecardScoresAggregation

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    response = api_instance.list_scorecard_scores(
        aggregation=ScorecardScoresAggregation.BY_ENTITY,
    )

    print(response)
