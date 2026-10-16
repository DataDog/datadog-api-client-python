# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.usage_quota_response_scope import UsageQuotaResponseScope


class UsageQuotaBulkResultAttributes(ModelNormal):
    validations = {
        "pending_effective_from": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_response_scope import UsageQuotaResponseScope

        return {
            "enforced": (bool,),
            "error": (str,),
            "org_public_id": (str,),
            "pending_effective_from": (str,),
            "pending_usage_limit": (float,),
            "scope": (UsageQuotaResponseScope,),
            "usage_limit": (float,),
        }

    attribute_map = {
        "enforced": "enforced",
        "error": "error",
        "org_public_id": "org_public_id",
        "pending_effective_from": "pending_effective_from",
        "pending_usage_limit": "pending_usage_limit",
        "scope": "scope",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_,
        enforced: Union[bool, UnsetType] = unset,
        error: Union[str, UnsetType] = unset,
        org_public_id: Union[str, UnsetType] = unset,
        pending_effective_from: Union[str, UnsetType] = unset,
        pending_usage_limit: Union[float, UnsetType] = unset,
        scope: Union[UsageQuotaResponseScope, UnsetType] = unset,
        usage_limit: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a usage quota bulk write result. On success, quota fields are present as applicable, and pending fields are present only when a change is scheduled. On failure, only ``error`` is present and the other fields are omitted.

        :param enforced: Whether usage above the limit is actively blocked instead of only tracked or alerted on. Omitted if this item failed to write.
        :type enforced: bool, optional

        :param error: An error message describing why this item failed to write. Omitted if this item was written successfully.
        :type error: str, optional

        :param org_public_id: The public ID of the organization that owns the quota. Omitted if this item failed to write.
        :type org_public_id: str, optional

        :param pending_effective_from: The future UTC month when the scheduled limit takes effect, formatted as ``YYYY-MM`` , starting at 00:00 UTC on its first day. Present only together with ``pending_usage_limit`` and omitted when no change is scheduled or this item failed to write.
        :type pending_effective_from: str, optional

        :param pending_usage_limit: The usage limit scheduled for the organization-wide quota in the usage units defined by the quota namespace. A value of ``0`` is valid. At the start of the effective month, this value becomes ``usage_limit`` and both pending fields are omitted. Omitted when no change is scheduled or this item failed to write.
        :type pending_usage_limit: float, optional

        :param scope: A namespace-specific key and value identifying what the quota applies to within an organization. The object contains exactly one entry. A value of ``"*"`` identifies the default quota applied to entities without a specific quota. This field is omitted for an organization-wide quota.
        :type scope: UsageQuotaResponseScope, optional

        :param usage_limit: The quota limit in the usage units defined by the quota namespace. May be fractional for quotas configured before public writes required whole units. Omitted if this item failed to write.
        :type usage_limit: float, optional
        """
        if enforced is not unset:
            kwargs["enforced"] = enforced
        if error is not unset:
            kwargs["error"] = error
        if org_public_id is not unset:
            kwargs["org_public_id"] = org_public_id
        if pending_effective_from is not unset:
            kwargs["pending_effective_from"] = pending_effective_from
        if pending_usage_limit is not unset:
            kwargs["pending_usage_limit"] = pending_usage_limit
        if scope is not unset:
            kwargs["scope"] = scope
        if usage_limit is not unset:
            kwargs["usage_limit"] = usage_limit
        super().__init__(kwargs)
