"""
Update an existing scorecard rule returns "Rule updated successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi
from datadog_api_client.v2.model.rule_attributes_request import RuleAttributesRequest
from datadog_api_client.v2.model.rule_type import RuleType
from datadog_api_client.v2.model.update_rule_request import UpdateRuleRequest
from datadog_api_client.v2.model.update_rule_request_data import UpdateRuleRequestData

body = UpdateRuleRequest(
    data=UpdateRuleRequestData(
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
    response = api_instance.update_scorecard_rule(rule_id="rule_id", body=body)

    print(response)
