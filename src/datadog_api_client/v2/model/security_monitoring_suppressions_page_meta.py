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


class SecurityMonitoringSuppressionsPageMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page_number": (int,),
            "page_size": (int,),
            "total_count": (int,),
        }

    attribute_map = {
        "page_number": "pageNumber",
        "page_size": "pageSize",
        "total_count": "totalCount",
    }

    def __init__(
        self_,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata.

        :param page_number: Current page number.
        :type page_number: int, optional

        :param page_size: Current page size.
        :type page_size: int, optional

        :param total_count: Total count of suppressions.
        :type total_count: int, optional
        """
        if page_number is not unset:
            kwargs["page_number"] = page_number
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
