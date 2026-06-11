"""
Get a user authorized client returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.user_authorized_clients_api import UserAuthorizedClientsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UserAuthorizedClientsApi(api_client)
    response = api_instance.get_user_authorized_client(
        user_authorized_client_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
