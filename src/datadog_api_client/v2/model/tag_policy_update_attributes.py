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
    from datadog_api_client.v2.model.tag_policy_type import TagPolicyType


class TagPolicyUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_type import TagPolicyType

        return {
            "enabled": (bool,),
            "negated": (bool,),
            "policy_name": (str,),
            "policy_type": (TagPolicyType,),
            "required": (bool,),
            "scope": (str,),
            "tag_key": (str,),
            "tag_value_patterns": ([str],),
        }

    attribute_map = {
        "enabled": "enabled",
        "negated": "negated",
        "policy_name": "policy_name",
        "policy_type": "policy_type",
        "required": "required",
        "scope": "scope",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        negated: Union[bool, UnsetType] = unset,
        policy_name: Union[str, UnsetType] = unset,
        policy_type: Union[TagPolicyType, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        tag_key: Union[str, UnsetType] = unset,
        tag_value_patterns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Mutable attributes of a tag policy. Each field is optional; omitting a field leaves its
        current value unchanged. The ``source`` of a policy cannot be changed.

        :param enabled: Whether the policy is currently enforced.
        :type enabled: bool, optional

        :param negated: When ``true`` , the policy matches tag values that do NOT match any of the supplied patterns.
        :type negated: bool, optional

        :param policy_name: Human-readable name for the tag policy.
        :type policy_name: str, optional

        :param policy_type: How the policy is enforced. ``blocking`` rejects telemetry that violates the policy.
            ``surfacing`` only highlights non-compliant telemetry without blocking it.
        :type policy_type: TagPolicyType, optional

        :param required: When ``true`` , telemetry without this tag is treated as a violation.
        :type required: bool, optional

        :param scope: The scope the policy applies within.
        :type scope: str, optional

        :param tag_key: The tag key that the policy governs.
        :type tag_key: str, optional

        :param tag_value_patterns: One or more patterns that valid values for the tag key must match.
        :type tag_value_patterns: [str], optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if negated is not unset:
            kwargs["negated"] = negated
        if policy_name is not unset:
            kwargs["policy_name"] = policy_name
        if policy_type is not unset:
            kwargs["policy_type"] = policy_type
        if required is not unset:
            kwargs["required"] = required
        if scope is not unset:
            kwargs["scope"] = scope
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if tag_value_patterns is not unset:
            kwargs["tag_value_patterns"] = tag_value_patterns
        super().__init__(kwargs)
