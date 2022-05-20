"""
Get all channels in a Slack integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.get_slack_integration_channels(
        account_name="account_name",
    )

    print(response)
