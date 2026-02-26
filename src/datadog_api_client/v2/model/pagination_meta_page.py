# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.pagination_meta_page_type import PaginationMetaPageType


class PaginationMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pagination_meta_page_type import PaginationMetaPageType

        return {
            "first_offset": (int,),
            "last_offset": (int, none_type),
            "limit": (int,),
            "next_offset": (int, none_type),
            "offset": (int,),
            "prev_offset": (int, none_type),
            "total": (int, none_type),
            "type": (PaginationMetaPageType,),
        }

    attribute_map = {
        "first_offset": "first_offset",
        "last_offset": "last_offset",
        "limit": "limit",
        "next_offset": "next_offset",
        "offset": "offset",
        "prev_offset": "prev_offset",
        "total": "total",
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
        total: Union[int, none_type, UnsetType] = unset,
        type: Union[PaginationMetaPageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Offset-based pagination schema.

        :param first_offset: Integer representing the offset to fetch the first page of results.
        :type first_offset: int, optional

        :param last_offset: Integer representing the offset to fetch the last page of results.
        :type last_offset: int, none_type, optional

        :param limit: Integer representing the number of elements to be returned in the results.
        :type limit: int, optional

        :param next_offset: Integer representing the index of the first element in the next page of results. Equal to page size added to the current offset.
        :type next_offset: int, none_type, optional

        :param offset: Integer representing the index of the first element in the results.
        :type offset: int, optional

        :param prev_offset: Integer representing the index of the first element in the previous page of results.
        :type prev_offset: int, none_type, optional

        :param total: Integer representing the total number of elements available.
        :type total: int, none_type, optional

        :param type:
        :type type: PaginationMetaPageType, optional
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
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
