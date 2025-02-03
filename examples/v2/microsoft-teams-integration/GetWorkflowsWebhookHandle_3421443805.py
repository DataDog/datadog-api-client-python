"""
Get workflow webhook handle information returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_workflows_webhook_handle(
        handle_id=WORKFLOWS_WEBHOOK_HANDLE_DATA_ID,
    )

    print(response)
