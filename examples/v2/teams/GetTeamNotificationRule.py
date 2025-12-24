"""
Get team notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = environ["TEAM_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_notification_rule(
        team_id=DD_TEAM_DATA_ID,
        rule_id=TEAM_NOTIFICATION_RULE_DATA_ID,
    )

    print(response)
