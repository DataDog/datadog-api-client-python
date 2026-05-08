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
    from datadog_api_client.v2.model.replay_analysis_signal import ReplayAnalysisSignal


class ReplayAnalysisIssueSessionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_signal import ReplayAnalysisSignal

        return {
            "session_start_timestamp_ms": (int,),
            "signals": ([ReplayAnalysisSignal],),
            "view_name": (str,),
        }

    attribute_map = {
        "session_start_timestamp_ms": "session_start_timestamp_ms",
        "signals": "signals",
        "view_name": "view_name",
    }

    def __init__(self_, session_start_timestamp_ms: int, signals: List[ReplayAnalysisSignal], view_name: str, **kwargs):
        """
        Attributes of a session related to a RUM replay analysis issue.

        :param session_start_timestamp_ms: Session start timestamp in milliseconds.
        :type session_start_timestamp_ms: int

        :param signals: List of signals observed in this session.
        :type signals: [ReplayAnalysisSignal]

        :param view_name: Name of the view where the issue was observed.
        :type view_name: str
        """
        super().__init__(kwargs)

        self_.session_start_timestamp_ms = session_start_timestamp_ms
        self_.signals = signals
        self_.view_name = view_name
