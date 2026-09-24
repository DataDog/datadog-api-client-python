"""
Create a new rule returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi
from datadog_api_client.v2.model.create_rule_request import CreateRuleRequest
from datadog_api_client.v2.model.create_rule_request_data import CreateRuleRequestData
from datadog_api_client.v2.model.rule_attributes_request import RuleAttributesRequest
from datadog_api_client.v2.model.rule_type import RuleType

body = CreateRuleRequest(
    data=CreateRuleRequestData(
        attributes=RuleAttributesRequest(
            enabled=True,
            name="Example-Scorecard",
            scorecard_name="Observability Best Practices",
        ),
        type=RuleType.RULE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    response = api_instance.create_scorecard_rule(body=body)

    print(response)
