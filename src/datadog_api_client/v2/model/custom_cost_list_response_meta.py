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


class CustomCostListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_filtered_count": (int,),
            "version": (str,),
        }

    attribute_map = {
        "total_filtered_count": "total_filtered_count",
        "version": "version",
    }

    def __init__(
        self_, total_filtered_count: Union[int, UnsetType] = unset, version: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Meta for the response from the List Custom Costs endpoints.

        :param total_filtered_count: Number of Custom Costs files returned by the List Custom Costs endpoint
        :type total_filtered_count: int, optional

        :param version: Version of Custom Costs file
        :type version: str, optional
        """
        if total_filtered_count is not unset:
            kwargs["total_filtered_count"] = total_filtered_count
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
