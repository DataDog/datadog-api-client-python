"""
List team connections returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    items = api_instance.list_team_connections_with_pagination()
    for item in items:
        print(item)
