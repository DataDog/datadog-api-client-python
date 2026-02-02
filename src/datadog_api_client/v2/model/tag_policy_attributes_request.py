# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TagPolicyAttributesRequest(ModelNormal):
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
        enabled: bool,
        negated: bool,
        policy_name: str,
        required: bool,
        scope: str,
        source: str,
        tag_key: str,
        tag_value_patterns: List[str],
        **kwargs,
    ):
        """
        Attributes for creating or updating a tag policy.

        :param enabled: Whether the policy is enabled.
        :type enabled: bool

        :param negated: Whether the policy is negated.
        :type negated: bool

        :param policy_name: The name of the tag policy.
        :type policy_name: str

        :param required: Whether the tag is required.
        :type required: bool

        :param scope: The scope of the tag policy.
        :type scope: str

        :param source: The data source for the tag policy (e.g., logs, metrics).
        :type source: str

        :param tag_key: The tag key that the policy applies to.
        :type tag_key: str

        :param tag_value_patterns: List of patterns that tag values must match.
        :type tag_value_patterns: [str]
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.negated = negated
        self_.policy_name = policy_name
        self_.required = required
        self_.scope = scope
        self_.source = source
        self_.tag_key = tag_key
        self_.tag_value_patterns = tag_value_patterns
