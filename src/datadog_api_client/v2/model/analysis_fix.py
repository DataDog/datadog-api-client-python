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
    from datadog_api_client.v2.model.analysis_edit import AnalysisEdit


class AnalysisFix(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_edit import AnalysisEdit

        return {
            "description": (str,),
            "edits": ([AnalysisEdit],),
        }

    attribute_map = {
        "description": "description",
        "edits": "edits",
    }

    def __init__(self_, description: str, edits: List[AnalysisEdit], **kwargs):
        """
        A fix suggestion for a rule violation, consisting of one or more edit operations.

        :param description: A human-readable description of what the fix does.
        :type description: str

        :param edits: The list of edit operations that constitute the fix.
        :type edits: [AnalysisEdit]
        """
        super().__init__(kwargs)

        self_.description = description
        self_.edits = edits
