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


class GraphItemDataAttributesCountsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "count": (int,),
        }

    attribute_map = {
        "column_name": "columnName",
        "count": "count",
    }

    def __init__(self_, column_name: Union[str, UnsetType] = unset, count: Union[int, UnsetType] = unset, **kwargs):
        """
        Count of devices for a single value of the grouping column in the End User Device Monitoring graph.

        :param column_name: Value of the grouping column for this bucket (for example, an operating system
            name or a device type).
        :type column_name: str, optional

        :param count: Number of devices that fall into this bucket.
        :type count: int, optional
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if count is not unset:
            kwargs["count"] = count
        super().__init__(kwargs)
