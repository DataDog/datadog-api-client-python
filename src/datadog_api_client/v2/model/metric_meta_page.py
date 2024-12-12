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
    from datadog_api_client.v2.model.metric_meta_page_type import MetricMetaPageType


class MetricMetaPage(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 20000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_meta_page_type import MetricMetaPageType

        return {
            "cursor": (str, none_type),
            "limit": (int,),
            "next_cursor": (str, none_type),
            "type": (MetricMetaPageType,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
        "next_cursor": "next_cursor",
        "type": "type",
    }

    def __init__(
        self_,
        cursor: Union[str, none_type, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_cursor: Union[str, none_type, UnsetType] = unset,
        type: Union[MetricMetaPageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Paging attributes. Only present if pagination query parameters were provided.

        :param cursor: The cursor used to get the current results, if any.
        :type cursor: str, none_type, optional

        :param limit: Number of results returned
        :type limit: int, optional

        :param next_cursor: The cursor used to get the next results, if any.
        :type next_cursor: str, none_type, optional

        :param type: Type of metric pagination.
        :type type: MetricMetaPageType, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
