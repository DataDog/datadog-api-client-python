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


class ListAPIsResponseMetaPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "limit": (int,),
            "offset": (int,),
            "total_count": (int,),
        }

    attribute_map = {
        "limit": "limit",
        "offset": "offset",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata information for ``ListAPIsResponse``.

        :param limit: Number of items in the current page.
        :type limit: int, optional

        :param offset: Offset for pagination.
        :type offset: int, optional

        :param total_count: Total number of items.
        :type total_count: int, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if offset is not unset:
            kwargs["offset"] = offset
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
