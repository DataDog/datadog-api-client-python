# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.control_notification_event_setting import ControlNotificationEventSetting


class ControlNotificationSettingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.control_notification_event_setting import ControlNotificationEventSetting

        return {
            "event_settings": ([ControlNotificationEventSetting],),
        }

    attribute_map = {
        "event_settings": "event_settings",
    }

    def __init__(self_, event_settings: List[ControlNotificationEventSetting], **kwargs):
        """
        The attributes of a governance control's notification settings.

        :param event_settings: The notification settings for each supported event type on the control.
        :type event_settings: [ControlNotificationEventSetting]
        """
        super().__init__(kwargs)

        self_.event_settings = event_settings
