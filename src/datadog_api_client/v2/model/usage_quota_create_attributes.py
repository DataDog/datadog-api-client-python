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
        "usage_limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_request_scope import UsageQuotaRequestScope

        return {
            "enforced": (bool,),
            "scope": (UsageQuotaRequestScope,),
            "usage_limit": (int,),
        }

    attribute_map = {
        "enforced": "enforced",
        "scope": "scope",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_, enforced: bool, usage_limit: int, scope: Union[UsageQuotaRequestScope, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for creating or updating a usage quota by scope.

        :param enforced: Whether to actively block usage above the limit instead of only tracking or alerting on it.
        :type enforced: bool

        :param scope: A namespace-specific key and value identifying what the quota applies to within an organization. The object must contain exactly one entry. Use ``"*"`` as the value for the default quota applied to entities without a specific quota, or omit the scope for an organization-wide quota. A specific value must identify an existing user handle in the caller's organization when ``include_descendants`` is false. When ``include_descendants`` is true, the handle must exist in the caller's organization or in at least one targeted descendant organization; the quota is then applied only to the organizations where that handle exists, and the request fails only if the handle exists in none of them.
        :type scope: UsageQuotaRequestScope, optional

        :param usage_limit: The quota limit to set in the usage units defined by the quota namespace. For an organization-wide quota (scope omitted), the limit must be greater than the usage already recorded in the current period.
        :type usage_limit: int
        """
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.enforced = enforced
        self_.usage_limit = usage_limit
