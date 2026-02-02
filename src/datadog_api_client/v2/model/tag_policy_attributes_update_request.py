# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TagPolicyAttributesUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "negated": (bool,),
            "policy_name": (str,),
            "required": (bool,),
            "scope": (str,),
            "source": (str,),
            "tag_key": (str,),
            "tag_value_patterns": ([str],),
        }

    attribute_map = {
        "enabled": "enabled",
        "negated": "negated",
        "policy_name": "policy_name",
        "required": "required",
        "scope": "scope",
        "source": "source",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        negated: Union[bool, UnsetType] = unset,
        policy_name: Union[str, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        tag_key: Union[str, UnsetType] = unset,
        tag_value_patterns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a tag policy. All fields are optional.

        :param enabled: Whether the policy is enabled.
        :type enabled: bool, optional

        :param negated: Whether the policy is negated.
        :type negated: bool, optional

        :param policy_name: The name of the tag policy.
        :type policy_name: str, optional

        :param required: Whether the tag is required.
        :type required: bool, optional

        :param scope: The scope of the tag policy.
        :type scope: str, optional

        :param source: The data source for the tag policy (e.g., logs, metrics).
        :type source: str, optional

        :param tag_key: The tag key that the policy applies to.
        :type tag_key: str, optional

        :param tag_value_patterns: List of patterns that tag values must match.
        :type tag_value_patterns: [str], optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if negated is not unset:
            kwargs["negated"] = negated
        if policy_name is not unset:
            kwargs["policy_name"] = policy_name
        if required is not unset:
            kwargs["required"] = required
        if scope is not unset:
            kwargs["scope"] = scope
        if source is not unset:
            kwargs["source"] = source
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if tag_value_patterns is not unset:
            kwargs["tag_value_patterns"] = tag_value_patterns
        super().__init__(kwargs)
