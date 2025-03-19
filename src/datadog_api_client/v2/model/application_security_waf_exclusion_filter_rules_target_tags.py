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


class ApplicationSecurityWafExclusionFilterRulesTargetTags(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

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
        Target multiple WAF rules based on their tags.

        :param category: The category of the targeted WAF rules.
        :type category: str, optional

        :param type: The type of the targeted WAF rules.
        :type type: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
