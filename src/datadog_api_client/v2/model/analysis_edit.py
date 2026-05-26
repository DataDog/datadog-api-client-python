# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.analysis_edit_type import AnalysisEditType
    from datadog_api_client.v2.model.analysis_position import AnalysisPosition


class AnalysisEdit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_edit_type import AnalysisEditType
        from datadog_api_client.v2.model.analysis_position import AnalysisPosition

        return {
            "content": (str, none_type),
            "edit_type": (AnalysisEditType,),
            "end": (AnalysisPosition,),
            "start": (AnalysisPosition,),
        }

    attribute_map = {
        "content": "content",
        "edit_type": "edit_type",
        "end": "end",
        "start": "start",
    }

    def __init__(
        self_,
        content: Union[str, none_type],
        edit_type: AnalysisEditType,
        end: AnalysisPosition,
        start: AnalysisPosition,
        **kwargs,
    ):
        """
        A single edit operation within a fix suggestion for a rule violation.

        :param content: The content to insert or replace at the specified position, if applicable.
        :type content: str, none_type

        :param edit_type: The type of code edit to apply when fixing a violation.
        :type edit_type: AnalysisEditType

        :param end: A position in source code, identified by line and column numbers.
        :type end: AnalysisPosition

        :param start: A position in source code, identified by line and column numbers.
        :type start: AnalysisPosition
        """
        super().__init__(kwargs)

        self_.content = content
        self_.edit_type = edit_type
        self_.end = end
        self_.start = start
