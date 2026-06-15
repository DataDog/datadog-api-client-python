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
    from datadog_api_client.v2.model.tag_policy_create_type import TagPolicyCreateType
    from datadog_api_client.v2.model.tag_policy_source import TagPolicySource


class TagPolicyCreateAttributes(ModelNormal):
    validations = {
        "tag_value_patterns": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_create_type import TagPolicyCreateType
        from datadog_api_client.v2.model.tag_policy_source import TagPolicySource

        return {
            "enabled": (bool,),
            "negated": (bool,),
            "policy_name": (str,),
            "policy_type": (TagPolicyCreateType,),
            "required": (bool,),
            "scope": (str,),
            "source": (TagPolicySource,),
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
        "source": "source",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
    }

    def __init__(
        self_,
        policy_name: str,
        policy_type: TagPolicyCreateType,
        scope: str,
        source: TagPolicySource,
        tag_key: str,
        tag_value_patterns: List[str],
        enabled: Union[bool, UnsetType] = unset,
        negated: Union[bool, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that can be supplied when creating a tag policy.

        :param enabled: Whether the policy is currently enforced. Defaults to ``true`` for newly created policies.
        :type enabled: bool, optional

        :param negated: When ``true`` , the policy matches tag values that do NOT match any of the supplied patterns. Defaults to ``false``.
        :type negated: bool, optional

        :param policy_name: Human-readable name for the tag policy.
        :type policy_name: str

        :param policy_type: The policy type allowed when creating a tag policy. Only ``surfacing`` is accepted at
            creation time.
        :type policy_type: TagPolicyCreateType

        :param required: When ``true`` , telemetry without this tag is treated as a violation. Defaults to ``false``.
        :type required: bool, optional

        :param scope: The scope the policy applies within. Typically an environment, team, or
            organization-level identifier used to limit where the policy is enforced.
        :type scope: str

        :param source: The telemetry source that a tag policy applies to.
        :type source: TagPolicySource

        :param tag_key: The tag key that the policy governs (for example, ``service`` ).
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

        self_.policy_name = policy_name
        self_.policy_type = policy_type
        self_.scope = scope
        self_.source = source
        self_.tag_key = tag_key
        self_.tag_value_patterns = tag_value_patterns
