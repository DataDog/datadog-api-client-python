"""
Update governance notification settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_settings_api import GovernanceSettingsApi
from datadog_api_client.v2.model.governance_notification_settings_resource_type import (
    GovernanceNotificationSettingsResourceType,
)
from datadog_api_client.v2.model.governance_notification_settings_update_attributes import (
    GovernanceNotificationSettingsUpdateAttributes,
)
from datadog_api_client.v2.model.governance_notification_settings_update_data import (
    GovernanceNotificationSettingsUpdateData,
)
from datadog_api_client.v2.model.governance_notification_settings_update_request import (
    GovernanceNotificationSettingsUpdateRequest,
)

body = GovernanceNotificationSettingsUpdateRequest(
    data=GovernanceNotificationSettingsUpdateData(
        attributes=GovernanceNotificationSettingsUpdateAttributes(
            assignment_notifications_enabled=True,
        ),
        type=GovernanceNotificationSettingsResourceType.GOVERNANCE_NOTIFICATION_SETTINGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_governance_notification_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceSettingsApi(api_client)
    response = api_instance.update_governance_notification_settings(body=body)

    print(response)
