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
    from datadog_api_client.v2.model.control_notification_target import ControlNotificationTarget


class ControlNotificationEventSetting(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.control_notification_target import ControlNotificationTarget

        return {
            "enabled": (bool,),
            "event_type": (str,),
            "targets": ([ControlNotificationTarget],),
        }

    attribute_map = {
        "enabled": "enabled",
        "event_type": "event_type",
        "targets": "targets",
    }

    def __init__(self_, enabled: bool, event_type: str, targets: List[ControlNotificationTarget], **kwargs):
        """
        The notification settings for a single event type on a control.

        :param enabled: Whether notifications are enabled for this event type.
        :type enabled: bool

        :param event_type: The event type the notification settings apply to, such as ``new_detection``.
        :type event_type: str

        :param targets: The destinations that receive notifications for an event type.
        :type targets: [ControlNotificationTarget]
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.event_type = event_type
        self_.targets = targets
