"""
Delete an external team permission default returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.external_team_permission_setting_defaults_source import (
    ExternalTeamPermissionSettingDefaultsSource,
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_external_team_permission_setting_default(
        source=ExternalTeamPermissionSettingDefaultsSource.SCIM,
        action="add_and_remove_subteam",
    )
