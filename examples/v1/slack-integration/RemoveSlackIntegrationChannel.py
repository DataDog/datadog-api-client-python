"""
Remove a Slack integration channel returns "The channel was removed successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    api_instance.remove_slack_integration_channel(
        account_name="account_name",
        channel_name="channel_name",
    )
