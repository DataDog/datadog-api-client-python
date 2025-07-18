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


class SingleAggregatedDnsResponseDataAttributesGroupByItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "value": (
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
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: Union[str, UnsetType] = unset, value: Union[Any, UnsetType] = unset, **kwargs):
        """
        Attributes associated with a group by

        :param key: The group by key.
        :type key: str, optional

        :param value: The group by value.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
