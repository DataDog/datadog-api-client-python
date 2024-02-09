"""
Get team memberships returns "Represents a user's association to a team" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    items = api_instance.get_team_memberships_with_pagination(
        team_id="2e06bf2c-193b-41d4-b3c2-afccc080458f",
        page_size=2,
    )
    for item in items:
        print(item)
