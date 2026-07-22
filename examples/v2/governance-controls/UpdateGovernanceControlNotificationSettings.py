"""
Update governance control notification settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi
from datadog_api_client.v2.model.control_notification_event_setting import ControlNotificationEventSetting
from datadog_api_client.v2.model.control_notification_settings_resource_type import (
    ControlNotificationSettingsResourceType,
)
from datadog_api_client.v2.model.control_notification_settings_update_attributes import (
    ControlNotificationSettingsUpdateAttributes,
)
from datadog_api_client.v2.model.control_notification_settings_update_data import ControlNotificationSettingsUpdateData
from datadog_api_client.v2.model.control_notification_settings_update_request import (
    ControlNotificationSettingsUpdateRequest,
)
from datadog_api_client.v2.model.control_notification_target import ControlNotificationTarget
from datadog_api_client.v2.model.control_notification_target_type import ControlNotificationTargetType

body = ControlNotificationSettingsUpdateRequest(
    data=ControlNotificationSettingsUpdateData(
        attributes=ControlNotificationSettingsUpdateAttributes(
            event_settings=[
                ControlNotificationEventSetting(
                    enabled=True,
                    event_type="new_detection",
                    targets=[
                        ControlNotificationTarget(
                            handle="#governance-alerts",
                            type=ControlNotificationTargetType.SLACK,
                        ),
                    ],
                ),
            ],
        ),
        type=ControlNotificationSettingsResourceType.CONTROL_NOTIFICATION_SETTINGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_governance_control_notification_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    response = api_instance.update_governance_control_notification_settings(detection_type="detection_type", body=body)

    print(response)
