# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AnalysisPosition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "col": (int,),
            "line": (int,),
        }

    attribute_map = {
        "col": "col",
        "line": "line",
    }

    def __init__(self_, col: int, line: int, **kwargs):
        """
        A position in source code, identified by line and column numbers.

        :param col: The column number in the source file (1-based).
        :type col: int

        :param line: The line number in the source file (1-based).
        :type line: int
        """
        super().__init__(kwargs)

        self_.col = col
        self_.line = line
