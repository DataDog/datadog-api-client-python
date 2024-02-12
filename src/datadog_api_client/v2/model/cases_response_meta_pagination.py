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


class CasesResponseMetaPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "current": (int,),
            "size": (int,),
            "total": (int,),
        }

    attribute_map = {
        "current": "current",
        "size": "size",
        "total": "total",
    }

    def __init__(
        self_,
        current: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata

        :param current: Current page number
        :type current: int, optional

        :param size: Number of cases in current page
        :type size: int, optional

        :param total: Total number of pages
        :type total: int, optional
        """
        if current is not unset:
            kwargs["current"] = current
        if size is not unset:
            kwargs["size"] = size
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
