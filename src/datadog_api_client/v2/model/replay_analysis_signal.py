# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ReplayAnalysisSignal(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event": (str,),
            "signal_type": (str,),
            "timestamp_ms": (int,),
            "user_pattern": (str,),
        }

    attribute_map = {
        "event": "event",
        "signal_type": "signal_type",
        "timestamp_ms": "timestamp_ms",
        "user_pattern": "user_pattern",
    }

    def __init__(self_, event: str, signal_type: str, timestamp_ms: int, user_pattern: str, **kwargs):
        """
        A signal associated with a replay issue, capturing user interaction details.

        :param event: Event name associated with the signal.
        :type event: str

        :param signal_type: Type of signal captured.
        :type signal_type: str

        :param timestamp_ms: Absolute timestamp of the signal in milliseconds.
        :type timestamp_ms: int

        :param user_pattern: User behavior pattern identified for the signal.
        :type user_pattern: str
        """
        super().__init__(kwargs)

        self_.event = event
        self_.signal_type = signal_type
        self_.timestamp_ms = timestamp_ms
        self_.user_pattern = user_pattern
