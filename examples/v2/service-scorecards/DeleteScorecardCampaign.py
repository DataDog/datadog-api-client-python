"""
Delete a campaign returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

configuration = Configuration()
configuration.unstable_operations["delete_scorecard_campaign"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.delete_scorecard_campaign(
        campaign_id="c10ODp0VCrrIpXmz",
    )
