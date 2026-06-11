"""
Delete all user authorized clients for a client returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.user_authorized_clients_api import UserAuthorizedClientsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UserAuthorizedClientsApi(api_client)
    api_instance.delete_user_authorized_clients_by_client(
        client_id="00000000-0000-0000-0000-000000000010",
    )
