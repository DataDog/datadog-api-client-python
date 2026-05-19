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


class ListScorecardScoresMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "limit": (int,),
            "offset": (int,),
            "total": (int,),
        }

    attribute_map = {
        "count": "count",
        "limit": "limit",
        "offset": "offset",
        "total": "total",
    }

    def __init__(
        self_,
        count: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata for scores.

        :param count: The number of results returned in this page.
        :type count: int, optional

        :param limit: The page limit.
        :type limit: int, optional

        :param offset: The page offset.
        :type offset: int, optional

        :param total: The total number of results.
        :type total: int, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if limit is not unset:
            kwargs["limit"] = limit
        if offset is not unset:
            kwargs["offset"] = offset
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
