"""
Get api handle information by name returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

# there is a valid "api_handle" in the system
API_HANDLE_DATA_ATTRIBUTES_NAME = environ["API_HANDLE_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_api_handle_by_name(
        handle_name=API_HANDLE_DATA_ATTRIBUTES_NAME,
    )

    print(response)
