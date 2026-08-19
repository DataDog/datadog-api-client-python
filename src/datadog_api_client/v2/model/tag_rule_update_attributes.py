# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tag_rule_type import TagRuleType


class TagRuleUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_type import TagRuleType

        return {
            "enabled": (bool,),
            "name": (str,),
            "negated": (bool,),
            "required": (bool,),
            "rule_type": (TagRuleType,),
            "scope": (str,),
            "tag_key": (str,),
            "tag_value_patterns": ([str],),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
        "negated": "negated",
        "required": "required",
        "rule_type": "rule_type",
        "scope": "scope",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        negated: Union[bool, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        rule_type: Union[TagRuleType, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        tag_key: Union[str, UnsetType] = unset,
        tag_value_patterns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Mutable attributes of a tag rule. Each field is optional; omitting a field leaves its
        current value unchanged. The ``source`` of a rule cannot be changed.

        :param enabled: Whether the rule is currently enforced.
        :type enabled: bool, optional

        :param name: Human-readable name for the tag rule.
        :type name: str, optional

        :param negated: When ``true`` , the rule matches tag values that do NOT match any of the supplied patterns.
        :type negated: bool, optional

        :param required: When ``true`` , telemetry without this tag is treated as a violation.
        :type required: bool, optional

        :param rule_type: How the rule is enforced. ``blocking`` rejects telemetry that violates the rule.
            ``surfacing`` only highlights non-compliant telemetry without blocking it.
        :type rule_type: TagRuleType, optional

        :param scope: The scope the rule applies within.
        :type scope: str, optional

        :param tag_key: The tag key that the rule governs.
        :type tag_key: str, optional

        :param tag_value_patterns: One or more patterns that valid values for the tag key must match.
        :type tag_value_patterns: [str], optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        if negated is not unset:
            kwargs["negated"] = negated
        if required is not unset:
            kwargs["required"] = required
        if rule_type is not unset:
            kwargs["rule_type"] = rule_type
        if scope is not unset:
            kwargs["scope"] = scope
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if tag_value_patterns is not unset:
            kwargs["tag_value_patterns"] = tag_value_patterns
        super().__init__(kwargs)
