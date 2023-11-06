"""
Create a new rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.create_rule_request import CreateRuleRequest
from datadog_api_client.v2.model.create_rule_request_data import CreateRuleRequestData
from datadog_api_client.v2.model.rule_attributes import RuleAttributes
from datadog_api_client.v2.model.rule_type import RuleType

body = CreateRuleRequest(
    data=CreateRuleRequestData(
        attributes=RuleAttributes(
            enabled=True,
            name="Example-Service-Scorecard",
            scorecard_name="Observability Best Practices",
        ),
        type=RuleType.RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_scorecard_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.create_scorecard_rule(body=body)

    print(response)
