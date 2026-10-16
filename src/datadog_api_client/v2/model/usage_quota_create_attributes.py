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
    from datadog_api_client.v2.model.usage_quota_request_scope import UsageQuotaRequestScope


class UsageQuotaCreateAttributes(ModelNormal):
    validations = {
        "pending_usage_limit": {
            "inclusive_minimum": 0,
        },
        "usage_limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_request_scope import UsageQuotaRequestScope

        return {
            "enforced": (bool,),
            "pending_usage_limit": (int,),
            "scope": (UsageQuotaRequestScope,),
            "usage_limit": (int,),
        }

    attribute_map = {
        "enforced": "enforced",
        "pending_usage_limit": "pending_usage_limit",
        "scope": "scope",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_,
        enforced: Union[bool, UnsetType] = unset,
        pending_usage_limit: Union[int, UnsetType] = unset,
        scope: Union[UsageQuotaRequestScope, UnsetType] = unset,
        usage_limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a usage quota by scope. Each item must provide ``usage_limit`` , ``pending_usage_limit`` , or both. Providing only ``pending_usage_limit`` updates an existing organization-wide quota, never creates one, requires ``enforced`` to be omitted, and fails if the quota does not exist.

        :param enforced: Whether to actively block usage above ``usage_limit`` instead of only tracking or alerting on it. Required when ``usage_limit`` is provided and must be omitted when only ``pending_usage_limit`` is provided.
        :type enforced: bool, optional

        :param pending_usage_limit: The non-negative, whole-number limit to schedule for the organization-wide quota in the usage units defined by the quota namespace. It is not checked against current usage. Each write schedules the value for 00:00 UTC on the first day of the next calendar month and replaces any previously scheduled change; the server computes ``pending_effective_from``. Omit this field to leave any scheduled change unchanged, including when raising ``usage_limit``. Cancel a scheduled change only by deleting the quota's ``/pending`` sub-resource.
        :type pending_usage_limit: int, optional

        :param scope: A namespace-specific key and value identifying what the quota applies to within an organization. The object must contain exactly one entry. Use ``"*"`` as the value for the default quota applied to entities without a specific quota, or omit the scope for an organization-wide quota. A specific value must identify an existing user handle in the caller's organization when ``include_descendants`` is false. When ``include_descendants`` is true, the handle must exist in the caller's organization or in at least one targeted descendant organization; the quota is then applied only to the organizations where that handle exists, and the request fails only if the handle exists in none of them.
        :type scope: UsageQuotaRequestScope, optional

        :param usage_limit: The non-negative, whole-number quota limit to set in the usage units defined by the quota namespace. For an organization-wide quota (scope omitted), the limit must be greater than usage already recorded in the current period. When this field is provided, ``enforced`` is required.
        :type usage_limit: int, optional
        """
        if enforced is not unset:
            kwargs["enforced"] = enforced
        if pending_usage_limit is not unset:
            kwargs["pending_usage_limit"] = pending_usage_limit
        if scope is not unset:
            kwargs["scope"] = scope
        if usage_limit is not unset:
            kwargs["usage_limit"] = usage_limit
        super().__init__(kwargs)
