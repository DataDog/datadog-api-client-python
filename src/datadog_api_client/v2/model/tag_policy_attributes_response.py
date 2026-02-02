# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class TagPolicyAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "enabled": (bool,),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "negated": (bool,),
            "policy_name": (str,),
            "required": (bool,),
            "scope": (str,),
            "source": (str,),
            "tag_key": (str,),
            "tag_value_patterns": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "negated": "negated",
        "policy_name": "policy_name",
        "required": "required",
        "scope": "scope",
        "source": "source",
        "tag_key": "tag_key",
        "tag_value_patterns": "tag_value_patterns",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        enabled: bool,
        modified_at: datetime,
        modified_by: str,
        negated: bool,
        policy_name: str,
        required: bool,
        scope: str,
        source: str,
        tag_key: str,
        tag_value_patterns: List[str],
        version: int,
        **kwargs,
    ):
        """
        Attributes of a tag policy response.

        :param created_at: Timestamp when the policy was created.
        :type created_at: datetime

        :param created_by: User who created the policy.
        :type created_by: str

        :param enabled: Whether the policy is enabled.
        :type enabled: bool

        :param modified_at: Timestamp when the policy was last modified.
        :type modified_at: datetime

        :param modified_by: User who last modified the policy.
        :type modified_by: str

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

        :param version: The version of the tag policy.
        :type version: int
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.negated = negated
        self_.policy_name = policy_name
        self_.required = required
        self_.scope = scope
        self_.source = source
        self_.tag_key = tag_key
        self_.tag_value_patterns = tag_value_patterns
        self_.version = version
