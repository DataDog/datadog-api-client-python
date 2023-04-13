"""
Update permission setting for team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_permission_setting_type import TeamPermissionSettingType
from datadog_api_client.v2.model.team_permission_setting_update import TeamPermissionSettingUpdate
from datadog_api_client.v2.model.team_permission_setting_update_attributes import TeamPermissionSettingUpdateAttributes
from datadog_api_client.v2.model.team_permission_setting_update_request import TeamPermissionSettingUpdateRequest
from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamPermissionSettingUpdateRequest(
    data=TeamPermissionSettingUpdate(
        attributes=TeamPermissionSettingUpdateAttributes(
            value=TeamPermissionSettingValue.ADMINS,
        ),
        type=TeamPermissionSettingType.TEAM_PERMISSION_SETTINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_permission_setting(
        team_id=DD_TEAM_DATA_ID, action="manage_membership", body=body
    )

    print(response)
