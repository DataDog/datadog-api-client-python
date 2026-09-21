# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MatchingSignalAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_tracker_id": (str,),
            "severity": (str,),
            "title": (str,),
            "trigger_time_ms": (int,),
        }

    attribute_map = {
        "event_tracker_id": "event_tracker_id",
        "severity": "severity",
        "title": "title",
        "trigger_time_ms": "trigger_time_ms",
    }

    def __init__(self_, event_tracker_id: str, severity: str, title: str, trigger_time_ms: int, **kwargs):
        """
        Attributes of a matching security signal.

        :param event_tracker_id: The tracker ID linking the signal back to the originating event. Distinct from ``id`` , which identifies the matching signal itself.
        :type event_tracker_id: str

        :param severity: The severity of the signal.
        :type severity: str

        :param title: The title of the signal.
        :type title: str

        :param trigger_time_ms: The Unix timestamp (in milliseconds) at which the signal was triggered.
        :type trigger_time_ms: int
        """
        super().__init__(kwargs)

        self_.event_tracker_id = event_tracker_id
        self_.severity = severity
        self_.title = title
        self_.trigger_time_ms = trigger_time_ms
