# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_tag_value_transform_type import ArbitraryRuleTagValueTransformType


class ArbitraryRuleTagValueTransform(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_tag_value_transform_type import (
            ArbitraryRuleTagValueTransformType,
        )

        return {
            "default": (str,),
            "map": ({str: (str,)},),
            "pattern": (str,),
            "replacement": (str,),
            "target": (str,),
            "type": (ArbitraryRuleTagValueTransformType,),
        }

    attribute_map = {
        "default": "default",
        "map": "map",
        "pattern": "pattern",
        "replacement": "replacement",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        type: ArbitraryRuleTagValueTransformType,
        default: Union[str, UnsetType] = unset,
        map: Union[Dict[str, str], UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        replacement: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A transform applied to the values of one tag key.

        :param default: The value used when no ``map`` entry matches.
        :type default: str, optional

        :param map: Lookup map from input value to output value, for ``lookup_map``.
        :type map: {str: (str,)}, optional

        :param pattern: The regular expression, for ``regex_extract`` and ``regex_replace``.
        :type pattern: str, optional

        :param replacement: The replacement string, for ``string_replace`` and ``regex_replace``.
        :type replacement: str, optional

        :param target: The substring to replace, for ``string_replace``.
        :type target: str, optional

        :param type: The kind of transform.
        :type type: ArbitraryRuleTagValueTransformType
        """
        if default is not unset:
            kwargs["default"] = default
        if map is not unset:
            kwargs["map"] = map
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if replacement is not unset:
            kwargs["replacement"] = replacement
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.type = type
