"""
Update team notification rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes
from datadog_api_client.v2.model.team_notification_rule_attributes_email import TeamNotificationRuleAttributesEmail
from datadog_api_client.v2.model.team_notification_rule_attributes_ms_teams import TeamNotificationRuleAttributesMsTeams
from datadog_api_client.v2.model.team_notification_rule_attributes_pagerduty import (
    TeamNotificationRuleAttributesPagerduty,
)
from datadog_api_client.v2.model.team_notification_rule_attributes_slack import TeamNotificationRuleAttributesSlack

body = TeamNotificationRule(
    attributes=TeamNotificationRuleAttributes(
        email=TeamNotificationRuleAttributesEmail(),
        ms_teams=TeamNotificationRuleAttributesMsTeams(),
        pagerduty=TeamNotificationRuleAttributesPagerduty(),
        slack=TeamNotificationRuleAttributesSlack(),
    ),
    id="b8626d7e-cedd-11eb-abf5-da7ad0900001",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_notification_rule(rule_id="rule_id", team_id="team_id", body=body)

    print(response)
