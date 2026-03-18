"""
Create a new rule returns "Created" response
"""

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
            level=2,
            name="Team Defined",
            scope_query="kind:service",
            scorecard_name="Deployments automated via Deployment Trains",
        ),
        type=RuleType.RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    response = api_instance.create_scorecard_rule(body=body)

    print(response)
