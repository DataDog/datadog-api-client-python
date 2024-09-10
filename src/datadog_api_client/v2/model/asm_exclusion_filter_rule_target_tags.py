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


class ASMExclusionFilterRuleTargetTags(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "type": (str,),
        }

    attribute_map = {
        "category": "category",
        "type": "type",
    }

    def __init__(self_, category: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs):
        """
        Tags identifying the category and type of the targeted rule.

        :param category: The category of the rule.
        :type category: str, optional

        :param type: The type of the rule.
        :type type: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
