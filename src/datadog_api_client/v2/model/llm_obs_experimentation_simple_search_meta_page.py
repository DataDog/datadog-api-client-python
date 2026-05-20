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


class LLMObsExperimentationSimpleSearchMetaPage(ModelNormal):
    validations = {
        "current": {
            "inclusive_maximum": 2147483647,
        },
        "limit": {
            "inclusive_maximum": 2147483647,
        },
        "total_count": {
            "inclusive_maximum": 2147483647,
        },
        "total_pages": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "current": (int,),
            "limit": (int,),
            "total_count": (int,),
            "total_pages": (int,),
        }

    attribute_map = {
        "current": "current",
        "limit": "limit",
        "total_count": "total_count",
        "total_pages": "total_pages",
    }

    def __init__(
        self_,
        current: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        total_pages: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Page metadata.

        :param current: Current page number.
        :type current: int, optional

        :param limit: Page size used for this response.
        :type limit: int, optional

        :param total_count: Total number of matching results (capped at the maximum search limit).
        :type total_count: int, optional

        :param total_pages: Total number of pages available.
        :type total_pages: int, optional
        """
        if current is not unset:
            kwargs["current"] = current
        if limit is not unset:
            kwargs["limit"] = limit
        if total_count is not unset:
            kwargs["total_count"] = total_count
        if total_pages is not unset:
            kwargs["total_pages"] = total_pages
        super().__init__(kwargs)
