# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FeatureFlagsPaginationMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first_offset": (int,),
            "last_offset": (int, none_type),
            "limit": (int,),
            "next_offset": (int, none_type),
            "offset": (int,),
            "prev_offset": (int, none_type),
            "total": (int,),
            "total_count": (int,),
            "total_filtered_count": (int,),
            "type": (str,),
        }

    attribute_map = {
        "first_offset": "first_offset",
        "last_offset": "last_offset",
        "limit": "limit",
        "next_offset": "next_offset",
        "offset": "offset",
        "prev_offset": "prev_offset",
        "total": "total",
        "total_count": "total_count",
        "total_filtered_count": "total_filtered_count",
        "type": "type",
    }

    def __init__(
        self_,
        first_offset: Union[int, UnsetType] = unset,
        last_offset: Union[int, none_type, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_offset: Union[int, none_type, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        prev_offset: Union[int, none_type, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        total_filtered_count: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata for feature flags list responses.

        :param first_offset: Offset of the first page.
        :type first_offset: int, optional

        :param last_offset: Offset of the last page.
        :type last_offset: int, none_type, optional

        :param limit: Maximum number of flags returned on this page.
        :type limit: int, optional

        :param next_offset: Offset of the next page, or null when there is no next page.
        :type next_offset: int, none_type, optional

        :param offset: Number of matching flags skipped before this page.
        :type offset: int, optional

        :param prev_offset: Offset of the previous page, or null when there is no previous page.
        :type prev_offset: int, none_type, optional

        :param total: Total number of flags matching the filters, independent of the page size.
        :type total: int, optional

        :param total_count: Legacy count field. Use ``total`` for the number of matching flags. **Deprecated**.
        :type total_count: int, optional

        :param total_filtered_count: Legacy filtered count field. Use ``total`` for the number of matching flags. **Deprecated**.
        :type total_filtered_count: int, optional

        :param type: The pagination method. Always ``offset_limit``.
        :type type: str, optional
        """
        if first_offset is not unset:
            kwargs["first_offset"] = first_offset
        if last_offset is not unset:
            kwargs["last_offset"] = last_offset
        if limit is not unset:
            kwargs["limit"] = limit
        if next_offset is not unset:
            kwargs["next_offset"] = next_offset
        if offset is not unset:
            kwargs["offset"] = offset
        if prev_offset is not unset:
            kwargs["prev_offset"] = prev_offset
        if total is not unset:
            kwargs["total"] = total
        if total_count is not unset:
            kwargs["total_count"] = total_count
        if total_filtered_count is not unset:
            kwargs["total_filtered_count"] = total_filtered_count
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
