# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.replay_analysis_llm_details import ReplayAnalysisLLMDetails
    from datadog_api_client.v2.model.replay_analysis_screenshot import ReplayAnalysisScreenshot
    from datadog_api_client.v2.model.replay_analysis_signal import ReplayAnalysisSignal


class ReplayAnalysisRepresentativeSession(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_llm_details import ReplayAnalysisLLMDetails
        from datadog_api_client.v2.model.replay_analysis_screenshot import ReplayAnalysisScreenshot
        from datadog_api_client.v2.model.replay_analysis_signal import ReplayAnalysisSignal

        return {
            "issue_category": (str,),
            "llm_analysis_details": (ReplayAnalysisLLMDetails,),
            "screenshot": (ReplayAnalysisScreenshot,),
            "session_id": (str,),
            "session_start_timestamp_ms": (int,),
            "signals": ([ReplayAnalysisSignal],),
            "view_name": (str, none_type),
        }

    attribute_map = {
        "issue_category": "issue_category",
        "llm_analysis_details": "llm_analysis_details",
        "screenshot": "screenshot",
        "session_id": "session_id",
        "session_start_timestamp_ms": "session_start_timestamp_ms",
        "signals": "signals",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        issue_category: str,
        llm_analysis_details: ReplayAnalysisLLMDetails,
        session_id: str,
        session_start_timestamp_ms: int,
        signals: List[ReplayAnalysisSignal],
        screenshot: Union[ReplayAnalysisScreenshot, UnsetType] = unset,
        view_name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A representative session illustrating a replay analysis issue.

        :param issue_category: Category of the issue observed in this session.
        :type issue_category: str

        :param llm_analysis_details: AI-generated analysis details for a replay issue.
        :type llm_analysis_details: ReplayAnalysisLLMDetails

        :param screenshot: A screenshot captured during a replay session.
        :type screenshot: ReplayAnalysisScreenshot, optional

        :param session_id: Unique identifier of the representative session.
        :type session_id: str

        :param session_start_timestamp_ms: Session start timestamp in milliseconds.
        :type session_start_timestamp_ms: int

        :param signals: List of signals observed in the representative session.
        :type signals: [ReplayAnalysisSignal]

        :param view_name: Name of the view where the issue was observed.
        :type view_name: str, none_type, optional
        """
        if screenshot is not unset:
            kwargs["screenshot"] = screenshot
        if view_name is not unset:
            kwargs["view_name"] = view_name
        super().__init__(kwargs)

        self_.issue_category = issue_category
        self_.llm_analysis_details = llm_analysis_details
        self_.session_id = session_id
        self_.session_start_timestamp_ms = session_start_timestamp_ms
        self_.signals = signals
