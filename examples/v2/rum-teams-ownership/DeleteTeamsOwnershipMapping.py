"""
Delete a teams ownership mapping returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_teams_ownership_api import RumTeamsOwnershipApi

# there is a valid "teams_ownership_mapping" in the system
TEAMS_OWNERSHIP_MAPPING_DATA_ID = environ["TEAMS_OWNERSHIP_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumTeamsOwnershipApi(api_client)
    api_instance.delete_teams_ownership_mapping(
        id=TEAMS_OWNERSHIP_MAPPING_DATA_ID,
    )
