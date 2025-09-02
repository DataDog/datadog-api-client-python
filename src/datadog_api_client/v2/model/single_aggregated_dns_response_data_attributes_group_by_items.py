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


class SingleAggregatedDnsResponseDataAttributesGroupByItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "value": (str,),
        }

    attribute_map = {
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: Union[str, UnsetType] = unset, value: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes associated with a group by

        :param key: The group by key.
        :type key: str, optional

        :param value: The group by value.
        :type value: str, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
