"""
List teams ownership rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_teams_ownership_api import RumTeamsOwnershipApi

# there is a valid "teams_ownership_mapping" in the system
TEAMS_OWNERSHIP_MAPPING_DATA_ATTRIBUTES_VIEW_NAME = environ["TEAMS_OWNERSHIP_MAPPING_DATA_ATTRIBUTES_VIEW_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumTeamsOwnershipApi(api_client)
    response = api_instance.list_teams_ownership_rules(
        filter_view_name=TEAMS_OWNERSHIP_MAPPING_DATA_ATTRIBUTES_VIEW_NAME,
    )

    print(response)
