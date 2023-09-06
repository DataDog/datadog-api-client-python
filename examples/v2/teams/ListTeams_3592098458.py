"""
Get all teams returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    items = api_instance.list_teams_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
