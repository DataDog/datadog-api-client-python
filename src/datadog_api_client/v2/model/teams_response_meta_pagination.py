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


class TeamsResponseMetaPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first_number": (int,),
            "first_offset": (int,),
            "last_number": (int, none_type),
            "last_offset": (int,),
            "limit": (int,),
            "next_number": (int, none_type),
            "next_offset": (int,),
            "number": (int,),
            "offset": (int,),
            "prev_number": (int, none_type),
            "prev_offset": (int,),
            "size": (int,),
            "total": (int,),
            "type": (str,),
        }

    attribute_map = {
        "first_number": "first_number",
        "first_offset": "first_offset",
        "last_number": "last_number",
        "last_offset": "last_offset",
        "limit": "limit",
        "next_number": "next_number",
        "next_offset": "next_offset",
        "number": "number",
        "offset": "offset",
        "prev_number": "prev_number",
        "prev_offset": "prev_offset",
        "size": "size",
        "total": "total",
        "type": "type",
    }

    def __init__(
        self_,
        first_number: Union[int, UnsetType] = unset,
        first_offset: Union[int, UnsetType] = unset,
        last_number: Union[int, none_type, UnsetType] = unset,
        last_offset: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_number: Union[int, none_type, UnsetType] = unset,
        next_offset: Union[int, UnsetType] = unset,
        number: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        prev_number: Union[int, none_type, UnsetType] = unset,
        prev_offset: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Teams response metadata.

        :param first_number: The first page number.
        :type first_number: int, optional

        :param first_offset: The first offset.
        :type first_offset: int, optional

        :param last_number: The last page number.
        :type last_number: int, none_type, optional

        :param last_offset: The last offset.
        :type last_offset: int, optional

        :param limit: Pagination limit.
        :type limit: int, optional

        :param next_number: The next page number.
        :type next_number: int, none_type, optional

        :param next_offset: The next offset.
        :type next_offset: int, optional

        :param number: The current page number, when page-number pagination is used.
        :type number: int, optional

        :param offset: The offset.
        :type offset: int, optional

        :param prev_number: The previous page number.
        :type prev_number: int, none_type, optional

        :param prev_offset: The previous offset.
        :type prev_offset: int, optional

        :param size: The page size, when page-number pagination is used.
        :type size: int, optional

        :param total: Total results.
        :type total: int, optional

        :param type: Pagination type. One of ``offset_limit`` or ``number_size``.
        :type type: str, optional
        """
        if first_number is not unset:
            kwargs["first_number"] = first_number
        if first_offset is not unset:
            kwargs["first_offset"] = first_offset
        if last_number is not unset:
            kwargs["last_number"] = last_number
        if last_offset is not unset:
            kwargs["last_offset"] = last_offset
        if limit is not unset:
            kwargs["limit"] = limit
        if next_number is not unset:
            kwargs["next_number"] = next_number
        if next_offset is not unset:
            kwargs["next_offset"] = next_offset
        if number is not unset:
            kwargs["number"] = number
        if offset is not unset:
            kwargs["offset"] = offset
        if prev_number is not unset:
            kwargs["prev_number"] = prev_number
        if prev_offset is not unset:
            kwargs["prev_offset"] = prev_offset
        if size is not unset:
            kwargs["size"] = size
        if total is not unset:
            kwargs["total"] = total
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
