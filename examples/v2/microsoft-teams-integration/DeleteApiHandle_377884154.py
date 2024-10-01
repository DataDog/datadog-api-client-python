"""
Delete api handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

# there is a valid "api_handle" in the system
API_HANDLE_DATA_ID = environ["API_HANDLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    api_instance.delete_api_handle(
        handle_id=API_HANDLE_DATA_ID,
    )
