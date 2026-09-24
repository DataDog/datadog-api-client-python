"""
List user authorized clients returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.user_authorized_clients_api import UserAuthorizedClientsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UserAuthorizedClientsApi(api_client)
    response = api_instance.list_user_authorized_clients()

    print(response)
