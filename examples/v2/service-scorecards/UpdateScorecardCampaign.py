"""
Update a campaign returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.campaign_type import CampaignType
from datadog_api_client.v2.model.update_campaign_request import UpdateCampaignRequest
from datadog_api_client.v2.model.update_campaign_request_attributes import UpdateCampaignRequestAttributes
from datadog_api_client.v2.model.update_campaign_request_data import UpdateCampaignRequestData
from datetime import datetime
from dateutil.tz import tzutc

body = UpdateCampaignRequest(
    data=UpdateCampaignRequestData(
        attributes=UpdateCampaignRequestAttributes(
            description="Campaign to improve security posture for Q1 2024.",
            due_date=datetime(2024, 3, 31, 23, 59, 59, tzinfo=tzutc()),
            entity_scope="kind:service AND team:platform",
            guidance="Please ensure all services pass the security requirements.",
            key="q1-security-2024",
            name="Q1 Security Campaign",
            owner_id="550e8400-e29b-41d4-a716-446655440000",
            rule_ids=[
                "q8MQxk8TCqrHnWkx",
                "r9NRyl9UDrsIoXly",
            ],
            start_date=datetime(2024, 1, 1, 0, 0, tzinfo=tzutc()),
            status="in_progress",
        ),
        type=CampaignType.CAMPAIGN,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_scorecard_campaign"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.update_scorecard_campaign(campaign_id="c10ODp0VCrrIpXmz", body=body)

    print(response)
