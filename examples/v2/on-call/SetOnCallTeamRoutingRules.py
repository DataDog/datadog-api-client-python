"""
Set On-Call team routing rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.send_slack_message_action import SendSlackMessageAction
from datadog_api_client.v2.model.send_slack_message_action_type import SendSlackMessageActionType
from datadog_api_client.v2.model.team_routing_rules_request import TeamRoutingRulesRequest
from datadog_api_client.v2.model.team_routing_rules_request_data import TeamRoutingRulesRequestData
from datadog_api_client.v2.model.team_routing_rules_request_data_attributes import TeamRoutingRulesRequestDataAttributes
from datadog_api_client.v2.model.team_routing_rules_request_data_type import TeamRoutingRulesRequestDataType
from datadog_api_client.v2.model.team_routing_rules_request_rule import TeamRoutingRulesRequestRule
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
from datadog_api_client.v2.model.urgency import Urgency
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]

body = TeamRoutingRulesRequest(
    data=TeamRoutingRulesRequestData(
        attributes=TeamRoutingRulesRequestDataAttributes(
            rules=[
                TeamRoutingRulesRequestRule(
                    actions=[
                        SendSlackMessageAction(
                            channel="channel",
                            type=SendSlackMessageActionType.SEND_SLACK_MESSAGE,
                            workspace="workspace",
                        ),
                    ],
                    query="tags.service:test",
                    time_restriction=TimeRestrictions(
                        time_zone="Europe/Paris",
                        restrictions=[
                            TimeRestriction(
                                end_day=Weekday.MONDAY,
                                end_time="17:00:00",
                                start_day=Weekday.MONDAY,
                                start_time="09:00:00",
                            ),
                            TimeRestriction(
                                end_day=Weekday.TUESDAY,
                                end_time="17:00:00",
                                start_day=Weekday.TUESDAY,
                                start_time="09:00:00",
                            ),
                        ],
                    ),
                ),
                TeamRoutingRulesRequestRule(
                    policy_id=ESCALATION_POLICY_DATA_ID,
                    query="",
                    urgency=Urgency.LOW,
                ),
            ],
        ),
        id=DD_TEAM_DATA_ID,
        type=TeamRoutingRulesRequestDataType.TEAM_ROUTING_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.set_on_call_team_routing_rules(team_id=DD_TEAM_DATA_ID, include="rules", body=body)

    print(response)
