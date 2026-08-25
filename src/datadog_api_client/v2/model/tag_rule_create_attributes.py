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
    from datadog_api_client.v2.model.tag_rule_create_type import TagRuleCreateType
    from datadog_api_client.v2.model.tag_rule_source import TagRuleSource


class TagRuleCreateAttributes(ModelNormal):
    validations = {
        "tag_value_patterns": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_create_type import TagRuleCreateType
        from datadog_api_client.v2.model.tag_rule_source import TagRuleSource

        return {
            "enabled": (bool,),
            "name": (str,),
            "negated": (bool,),
            "required": (bool,),
            "rule_type": (TagRuleCreateType,),
            "scope": (str,),
            "source": (TagRuleSource,),
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
        "source": "source",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
    }

    def __init__(
        self_,
        name: str,
        rule_type: TagRuleCreateType,
        scope: str,
        source: TagRuleSource,
        tag_key: str,
        tag_value_patterns: List[str],
        enabled: Union[bool, UnsetType] = unset,
        negated: Union[bool, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that can be supplied when creating a tag rule.

        :param enabled: Whether the rule is currently enforced. Defaults to ``true`` for newly created rules.
        :type enabled: bool, optional

        :param name: Human-readable name for the tag rule.
        :type name: str

        :param negated: When ``true`` , the rule matches tag values that do NOT match any of the supplied patterns. Defaults to ``false``.
        :type negated: bool, optional

        :param required: When ``true`` , telemetry without this tag is treated as a violation. Defaults to ``false``.
        :type required: bool, optional

        :param rule_type: The rule type allowed when creating a tag rule. Only ``surfacing`` is accepted at
            creation time.
        :type rule_type: TagRuleCreateType

        :param scope: The scope the rule applies within. Typically an environment, team, or
            organization-level identifier used to limit where the rule is enforced.
        :type scope: str

        :param source: The telemetry source that a tag rule applies to.
        :type source: TagRuleSource

        :param tag_key: The tag key that the rule governs (for example, ``service`` ).
        :type tag_key: str

        :param tag_value_patterns: One or more patterns that valid values for the tag key must match. At least one
            pattern is required.
        :type tag_value_patterns: [str]
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if negated is not unset:
            kwargs["negated"] = negated
        if required is not unset:
            kwargs["required"] = required
        super().__init__(kwargs)

        self_.name = name
        self_.rule_type = rule_type
        self_.scope = scope
        self_.source = source
        self_.tag_key = tag_key
        self_.tag_value_patterns = tag_value_patterns
