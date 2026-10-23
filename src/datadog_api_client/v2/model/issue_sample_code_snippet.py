# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IssueSampleCodeSnippet(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "lines": ([str],),
            "offset": (int,),
        }

    attribute_map = {
        "lines": "lines",
        "offset": "offset",
    }

    def __init__(self_, lines: Union[List[str], UnsetType] = unset, offset: Union[int, UnsetType] = unset, **kwargs):
        """
        Source code around a stack frame. Empty when the source code is unavailable.

        :param lines: Lines of source code.
        :type lines: [str], optional

        :param offset: Line number of the first line of the snippet, starting at 1.
        :type offset: int, optional
        """
        if lines is not unset:
            kwargs["lines"] = lines
        if offset is not unset:
            kwargs["offset"] = offset
        super().__init__(kwargs)
