# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ArbitraryRuleResponseDataAttributesCostsToAllocateItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "condition": (str,),
            "tag": (str,),
            "value": (str,),
            "values": ([str], none_type),
        }

    attribute_map = {
        "condition": "condition",
        "tag": "tag",
        "value": "value",
        "values": "values",
    }

    def __init__(
        self_,
        condition: str,
        tag: str,
        value: Union[str, UnsetType] = unset,
        values: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleResponseDataAttributesCostsToAllocateItems`` object.

        :param condition: The ``items`` ``condition``.
        :type condition: str

        :param tag: The ``items`` ``tag``.
        :type tag: str

        :param value: The ``items`` ``value``.
        :type value: str, optional

        :param values: The ``items`` ``values``.
        :type values: [str], none_type, optional
        """
        if value is not unset:
            kwargs["value"] = value
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)

        self_.condition = condition
        self_.tag = tag
