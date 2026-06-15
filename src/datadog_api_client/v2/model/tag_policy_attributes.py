# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tag_policy_type import TagPolicyType
    from datadog_api_client.v2.model.tag_policy_source import TagPolicySource


class TagPolicyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_type import TagPolicyType
        from datadog_api_client.v2.model.tag_policy_source import TagPolicySource

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "deleted_at": (datetime, none_type),
            "deleted_by": (str, none_type),
            "enabled": (bool,),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "negated": (bool,),
            "policy_name": (str,),
            "policy_type": (TagPolicyType,),
            "required": (bool,),
            "scope": (str,),
            "source": (TagPolicySource,),
            "tag_key": (str,),
            "tag_value_patterns": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "deleted_at": "deleted_at",
        "deleted_by": "deleted_by",
        "enabled": "enabled",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "negated": "negated",
        "policy_name": "policy_name",
        "policy_type": "policy_type",
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
        policy_type: TagPolicyType,
        required: bool,
        scope: str,
        source: TagPolicySource,
        tag_key: str,
        tag_value_patterns: List[str],
        version: int,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        deleted_by: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a tag policy resource.

        :param created_at: The RFC 3339 timestamp at which the policy was created.
        :type created_at: datetime

        :param created_by: The identifier of the user who created the policy.
        :type created_by: str

        :param deleted_at: The RFC 3339 timestamp at which the policy was soft-deleted. ``null`` if the policy has not been deleted. Only present when ``include_deleted=true`` is requested.
        :type deleted_at: datetime, none_type, optional

        :param deleted_by: The identifier of the user who soft-deleted the policy. ``null`` if the policy has not been deleted.
        :type deleted_by: str, none_type, optional

        :param enabled: Whether the policy is currently enforced.
        :type enabled: bool

        :param modified_at: The RFC 3339 timestamp at which the policy was last modified.
        :type modified_at: datetime

        :param modified_by: The identifier of the user who last modified the policy.
        :type modified_by: str

        :param negated: When ``true`` , the policy matches tag values that do NOT match any of the supplied patterns.
        :type negated: bool

        :param policy_name: Human-readable name for the tag policy.
        :type policy_name: str

        :param policy_type: How the policy is enforced. ``blocking`` rejects telemetry that violates the policy.
            ``surfacing`` only highlights non-compliant telemetry without blocking it.
        :type policy_type: TagPolicyType

        :param required: When ``true`` , telemetry without this tag is treated as a violation.
        :type required: bool

        :param scope: The scope the policy applies within.
        :type scope: str

        :param source: The telemetry source that a tag policy applies to.
        :type source: TagPolicySource

        :param tag_key: The tag key that the policy governs.
        :type tag_key: str

        :param tag_value_patterns: The patterns that valid values for the tag key must match.
        :type tag_value_patterns: [str]

        :param version: A monotonically increasing version counter that is incremented on each update.
        :type version: int
        """
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if deleted_by is not unset:
            kwargs["deleted_by"] = deleted_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.negated = negated
        self_.policy_name = policy_name
        self_.policy_type = policy_type
        self_.required = required
        self_.scope = scope
        self_.source = source
        self_.tag_key = tag_key
        self_.tag_value_patterns = tag_value_patterns
        self_.version = version
