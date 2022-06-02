"""
Update a Slack integration channel returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi
from datadog_api_client.v1.model.slack_integration_channel import SlackIntegrationChannel
from datadog_api_client.v1.model.slack_integration_channel_display import SlackIntegrationChannelDisplay

body = SlackIntegrationChannel(
    display=SlackIntegrationChannelDisplay(
        message=True,
        notified=True,
        snapshot=True,
        tags=True,
    ),
    name="#general",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.update_slack_integration_channel(
        account_name="account_name", channel_name="channel_name", body=body
    )

    print(response)
