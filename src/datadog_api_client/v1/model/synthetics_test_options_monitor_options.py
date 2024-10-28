# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_test_options_monitor_options_notification_preset_name import (
        SyntheticsTestOptionsMonitorOptionsNotificationPresetName,
    )


class SyntheticsTestOptionsMonitorOptions(ModelNormal):
    validations = {
        "renotify_interval": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_options_monitor_options_notification_preset_name import (
            SyntheticsTestOptionsMonitorOptionsNotificationPresetName,
        )

        return {
            "escalation_message": (str,),
            "notification_preset_name": (SyntheticsTestOptionsMonitorOptionsNotificationPresetName,),
            "renotify_interval": (int,),
            "renotify_occurrences": (int,),
        }

    attribute_map = {
        "escalation_message": "escalation_message",
        "notification_preset_name": "notification_preset_name",
        "renotify_interval": "renotify_interval",
        "renotify_occurrences": "renotify_occurrences",
    }

    def __init__(
        self_,
        escalation_message: Union[str, UnsetType] = unset,
        notification_preset_name: Union[SyntheticsTestOptionsMonitorOptionsNotificationPresetName, UnsetType] = unset,
        renotify_interval: Union[int, UnsetType] = unset,
        renotify_occurrences: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the options for a Synthetic test as a monitor
        (for example, renotification).

        :param escalation_message: Message to include in the escalation notification.
        :type escalation_message: str, optional

        :param notification_preset_name: The name of the preset for the notification for the monitor.
        :type notification_preset_name: SyntheticsTestOptionsMonitorOptionsNotificationPresetName, optional

        :param renotify_interval: Time interval before renotifying if the test is still failing
            (in minutes).
        :type renotify_interval: int, optional

        :param renotify_occurrences: The number of times to renotify if the test is still failing.
        :type renotify_occurrences: int, optional
        """
        if escalation_message is not unset:
            kwargs["escalation_message"] = escalation_message
        if notification_preset_name is not unset:
            kwargs["notification_preset_name"] = notification_preset_name
        if renotify_interval is not unset:
            kwargs["renotify_interval"] = renotify_interval
        if renotify_occurrences is not unset:
            kwargs["renotify_occurrences"] = renotify_occurrences
        super().__init__(kwargs)
