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


class ListFindingsPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "cursor": "cursor",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(
        self_, cursor: Union[str, UnsetType] = unset, total_filtered_count: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Pagination and findings count information.

        :param cursor: The cursor used to paginate requests.
        :type cursor: str, optional

        :param total_filtered_count: The total count of findings after the filter has been applied.
        :type total_filtered_count: int, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if total_filtered_count is not unset:
            kwargs["total_filtered_count"] = total_filtered_count
        super().__init__(kwargs)
