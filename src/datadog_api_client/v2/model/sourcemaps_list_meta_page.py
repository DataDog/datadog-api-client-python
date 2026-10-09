# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SourcemapsListMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_more_results": (bool,),
            "next_cursor": (str,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "has_more_results": "has_more_results",
        "next_cursor": "next_cursor",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(
        self_, has_more_results: bool, total_filtered_count: int, next_cursor: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Page information for the source maps list response.

        :param has_more_results: Whether there are more results available beyond the current page.
        :type has_more_results: bool

        :param next_cursor: Cursor for the next page of a JavaScript cursor-based listing. Pass
            this value as ``page[after]`` with the same search mode and filters.
            Only returned when another page is available.
        :type next_cursor: str, optional

        :param total_filtered_count: Total number of matching source maps for legacy page-number pagination.
            Cursor-based listings do not compute a total; this field may be zero
            even when records are returned. Use ``has_more_results`` to continue.
        :type total_filtered_count: int
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)

        self_.has_more_results = has_more_results
        self_.total_filtered_count = total_filtered_count
