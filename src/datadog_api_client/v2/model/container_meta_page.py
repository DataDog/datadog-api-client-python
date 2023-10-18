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
    from datadog_api_client.v2.model.container_meta_page_type import ContainerMetaPageType


class ContainerMetaPage(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 10000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_meta_page_type import ContainerMetaPageType

        return {
            "cursor": (str,),
            "limit": (int,),
            "next_cursor": (str,),
            "prev_cursor": (str, none_type),
            "total": (int,),
            "type": (ContainerMetaPageType,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
        "next_cursor": "next_cursor",
        "prev_cursor": "prev_cursor",
        "total": "total",
        "type": "type",
    }

    def __init__(
        self_,
        cursor: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_cursor: Union[str, UnsetType] = unset,
        prev_cursor: Union[str, none_type, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        type: Union[ContainerMetaPageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Paging attributes.

        :param cursor: The cursor used to get the current results, if any.
        :type cursor: str, optional

        :param limit: Number of results returned
        :type limit: int, optional

        :param next_cursor: The cursor used to get the next results, if any.
        :type next_cursor: str, optional

        :param prev_cursor: The cursor used to get the previous results, if any.
        :type prev_cursor: str, none_type, optional

        :param total: Total number of records that match the query.
        :type total: int, optional

        :param type: Type of Container pagination.
        :type type: ContainerMetaPageType, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        if prev_cursor is not unset:
            kwargs["prev_cursor"] = prev_cursor
        if total is not unset:
            kwargs["total"] = total
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
