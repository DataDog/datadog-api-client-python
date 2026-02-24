"""
Generate team-specific campaign reports returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.entity_owner_destination import EntityOwnerDestination
from datadog_api_client.v2.model.generate_campaign_team_reports_request import GenerateCampaignTeamReportsRequest
from datadog_api_client.v2.model.generate_campaign_team_reports_request_attributes import (
    GenerateCampaignTeamReportsRequestAttributes,
)
from datadog_api_client.v2.model.generate_campaign_team_reports_request_data import (
    GenerateCampaignTeamReportsRequestData,
)
from datadog_api_client.v2.model.generate_campaign_team_reports_request_data_type import (
    GenerateCampaignTeamReportsRequestDataType,
)
from datadog_api_client.v2.model.slack_routing_options import SlackRoutingOptions

body = GenerateCampaignTeamReportsRequest(
    data=GenerateCampaignTeamReportsRequestData(
        attributes=GenerateCampaignTeamReportsRequestAttributes(
            entity_owners=[
                EntityOwnerDestination(
                    slack=SlackRoutingOptions(
                        channel_id="C024BDQ4N",
                        workspace_id="T024BDQ4N",
                    ),
                    team_id="550e8400-e29b-41d4-a716-446655440000",
                ),
            ],
        ),
        type=GenerateCampaignTeamReportsRequestDataType.CAMPAIGN_TEAM_REPORT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["generate_scorecard_campaign_team_reports"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.generate_scorecard_campaign_team_reports(campaign_id="c10ODp0VCrrIpXmz", body=body)
