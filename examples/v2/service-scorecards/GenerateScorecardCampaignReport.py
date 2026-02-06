"""
Generate campaign report returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.generate_campaign_report_request import GenerateCampaignReportRequest
from datadog_api_client.v2.model.generate_campaign_report_request_attributes import (
    GenerateCampaignReportRequestAttributes,
)
from datadog_api_client.v2.model.generate_campaign_report_request_data import GenerateCampaignReportRequestData
from datadog_api_client.v2.model.generate_campaign_report_request_data_type import GenerateCampaignReportRequestDataType
from datadog_api_client.v2.model.slack_routing_options import SlackRoutingOptions

body = GenerateCampaignReportRequest(
    data=GenerateCampaignReportRequestData(
        attributes=GenerateCampaignReportRequestAttributes(
            slack=SlackRoutingOptions(
                channel_id="C024BDQ4N",
                channel_name="service-scorecards",
                workspace_id="T024BDQ4N",
                workspace_name="datadog-workspace",
            ),
        ),
        type=GenerateCampaignReportRequestDataType.CAMPAIGN_REPORT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["generate_scorecard_campaign_report"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.generate_scorecard_campaign_report(campaign_id="c10ODp0VCrrIpXmz", body=body)
