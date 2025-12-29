"""
Create team notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes
from datadog_api_client.v2.model.team_notification_rule_attributes_email import TeamNotificationRuleAttributesEmail
from datadog_api_client.v2.model.team_notification_rule_attributes_slack import TeamNotificationRuleAttributesSlack
from datadog_api_client.v2.model.team_notification_rule_request import TeamNotificationRuleRequest
from datadog_api_client.v2.model.team_notification_rule_type import TeamNotificationRuleType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamNotificationRuleRequest(
    data=TeamNotificationRule(
        type=TeamNotificationRuleType.TEAM_NOTIFICATION_RULES,
        attributes=TeamNotificationRuleAttributes(
            email=TeamNotificationRuleAttributesEmail(
                enabled=True,
            ),
            slack=TeamNotificationRuleAttributesSlack(
                workspace="Datadog",
                channel="aaa-omg-ops",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_notification_rule(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
