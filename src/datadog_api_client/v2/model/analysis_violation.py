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
    from datadog_api_client.v2.model.analysis_position import AnalysisPosition
    from datadog_api_client.v2.model.analysis_fix import AnalysisFix


class AnalysisViolation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_position import AnalysisPosition
        from datadog_api_client.v2.model.analysis_fix import AnalysisFix

        return {
            "category": (str,),
            "end": (AnalysisPosition,),
            "fixes": ([AnalysisFix],),
            "message": (str,),
            "severity": (str,),
            "start": (AnalysisPosition,),
        }

    attribute_map = {
        "category": "category",
        "end": "end",
        "fixes": "fixes",
        "message": "message",
        "severity": "severity",
        "start": "start",
    }

    def __init__(
        self_,
        category: str,
        end: AnalysisPosition,
        fixes: List[AnalysisFix],
        message: str,
        severity: str,
        start: AnalysisPosition,
        **kwargs,
    ):
        """
        A rule violation found in the analyzed source code.

        :param category: The category of the violation.
        :type category: str

        :param end: A position in source code, identified by line and column numbers.
        :type end: AnalysisPosition

        :param fixes: The list of suggested fixes for this violation.
        :type fixes: [AnalysisFix]

        :param message: A human-readable description of the violation.
        :type message: str

        :param severity: The severity level of the violation.
        :type severity: str

        :param start: A position in source code, identified by line and column numbers.
        :type start: AnalysisPosition
        """
        super().__init__(kwargs)

        self_.category = category
        self_.end = end
        self_.fixes = fixes
        self_.message = message
        self_.severity = severity
        self_.start = start
