"""
Get a campaign returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scorecards_api import ScorecardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScorecardsApi(api_client)
    response = api_instance.get_scorecard_campaign(
        campaign_id="c10ODp0VCrrIpXmz",
    )

    print(response)
