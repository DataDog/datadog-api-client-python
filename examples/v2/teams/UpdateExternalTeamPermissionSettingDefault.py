"""
Update an external team permission default returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.external_team_permission_setting_default_update_attributes import (
    ExternalTeamPermissionSettingDefaultUpdateAttributes,
)
from datadog_api_client.v2.model.external_team_permission_setting_default_update_data import (
    ExternalTeamPermissionSettingDefaultUpdateData,
)
from datadog_api_client.v2.model.external_team_permission_setting_default_update_request import (
    ExternalTeamPermissionSettingDefaultUpdateRequest,
)
from datadog_api_client.v2.model.external_team_permission_setting_defaults_source import (
    ExternalTeamPermissionSettingDefaultsSource,
)
from datadog_api_client.v2.model.external_team_permission_setting_defaults_type import (
    ExternalTeamPermissionSettingDefaultsType,
)

body = ExternalTeamPermissionSettingDefaultUpdateRequest(
    data=ExternalTeamPermissionSettingDefaultUpdateData(
        attributes=ExternalTeamPermissionSettingDefaultUpdateAttributes(
            value="user_access_manage",
        ),
        id="scim:add_and_remove_subteam",
        type=ExternalTeamPermissionSettingDefaultsType.EXTERNAL_TEAM_PERMISSION_SETTING_DEFAULTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_external_team_permission_setting_default(
        source=ExternalTeamPermissionSettingDefaultsSource.SCIM, action="add_and_remove_subteam", body=body
    )

    print(response)
