# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.control_notification_event_setting import ControlNotificationEventSetting


class ControlNotificationSettingsUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.control_notification_event_setting import ControlNotificationEventSetting

        return {
            "event_settings": ([ControlNotificationEventSetting],),
        }

    attribute_map = {
        "event_settings": "event_settings",
    }

    def __init__(self_, event_settings: Union[List[ControlNotificationEventSetting], UnsetType] = unset, **kwargs):
        """
        The attributes of a governance control's notification settings that can be updated.

        :param event_settings: The notification settings for each supported event type on the control.
        :type event_settings: [ControlNotificationEventSetting], optional
        """
        if event_settings is not unset:
            kwargs["event_settings"] = event_settings
        super().__init__(kwargs)
