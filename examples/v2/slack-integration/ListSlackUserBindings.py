"""
List Slack user bindings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.slack_integration_api import SlackIntegrationApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.list_slack_user_bindings(
        user_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
