"""
Update api handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_api_handle_attributes import MicrosoftTeamsApiHandleAttributes
from datadog_api_client.v2.model.microsoft_teams_api_handle_type import MicrosoftTeamsApiHandleType
from datadog_api_client.v2.model.microsoft_teams_update_api_handle_request import MicrosoftTeamsUpdateApiHandleRequest
from datadog_api_client.v2.model.microsoft_teams_update_api_handle_request_data import (
    MicrosoftTeamsUpdateApiHandleRequestData,
)

# there is a valid "api_handle" in the system
API_HANDLE_DATA_ATTRIBUTES_NAME = environ["API_HANDLE_DATA_ATTRIBUTES_NAME"]
API_HANDLE_DATA_ID = environ["API_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateApiHandleRequest(
    data=MicrosoftTeamsUpdateApiHandleRequestData(
        attributes=MicrosoftTeamsApiHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsApiHandleType.HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_api_handle(handle_id=API_HANDLE_DATA_ID, body=body)

    print(response)
