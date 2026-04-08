"""
Delete a rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    api_instance.delete_scorecard_rule(
        rule_id=CREATE_SCORECARD_RULE_DATA_ID,
    )
