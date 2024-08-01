"""
Update an existing rule returns "Rule updated successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.rule_attributes import RuleAttributes
from datadog_api_client.v2.model.update_rule_request import UpdateRuleRequest
from datadog_api_client.v2.model.update_rule_request_data import UpdateRuleRequestData

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME = environ["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME"]
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME = environ["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME"]
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = UpdateRuleRequest(
    data=UpdateRuleRequestData(
        attributes=RuleAttributes(
            enabled=True,
            name=CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME,
            scorecard_name=CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME,
            description="Updated description via test",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_scorecard_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.update_scorecard_rule(rule_id=CREATE_SCORECARD_RULE_DATA_ID, body=body)

    print(response)
