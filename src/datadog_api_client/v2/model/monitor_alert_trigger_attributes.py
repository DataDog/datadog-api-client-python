# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorAlertTriggerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_id": (str,),
            "event_ts": (int,),
            "monitor_id": (int,),
        }

    attribute_map = {
        "event_id": "event_id",
        "event_ts": "event_ts",
        "monitor_id": "monitor_id",
    }

    def __init__(self_, event_id: str, event_ts: int, monitor_id: int, **kwargs):
        """
        Attributes for a monitor alert trigger.

        :param event_id: The event ID associated with the monitor alert.
        :type event_id: str

        :param event_ts: The timestamp of the event in Unix milliseconds.
        :type event_ts: int

        :param monitor_id: The monitor ID that triggered the alert.
        :type monitor_id: int
        """
        super().__init__(kwargs)

        self_.event_id = event_id
        self_.event_ts = event_ts
        self_.monitor_id = monitor_id
