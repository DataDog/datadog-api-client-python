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


class PowerpacksResponseMetaPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first_offset": (int,),
            "last_offset": (int, none_type),
            "limit": (int,),
            "next_offset": (int,),
            "offset": (int,),
            "prev_offset": (int,),
            "total": (int,),
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
        "type": "type",
    }

    def __init__(
        self_,
        first_offset: Union[int, UnsetType] = unset,
        last_offset: Union[int, none_type, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_offset: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        prev_offset: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack response pagination metadata.

        :param first_offset: The first offset.
        :type first_offset: int, optional

        :param last_offset: The last offset.
        :type last_offset: int, none_type, optional

        :param limit: Pagination limit.
        :type limit: int, optional

        :param next_offset: The next offset.
        :type next_offset: int, optional

        :param offset: The offset.
        :type offset: int, optional

        :param prev_offset: The previous offset.
        :type prev_offset: int, optional

        :param total: Total results.
        :type total: int, optional

        :param type: Offset type.
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
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
