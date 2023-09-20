# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class MonitorSearchCountItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "name": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "count": "count",
        "name": "name",
    }
    read_only_vars = {
        "count",
        "name",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, name: Union[Any, UnsetType] = unset, **kwargs):
        """
        A facet item.

        :param count: The number of found monitors with the listed value.
        :type count: int, optional

        :param name: The facet value.
        :type name: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
