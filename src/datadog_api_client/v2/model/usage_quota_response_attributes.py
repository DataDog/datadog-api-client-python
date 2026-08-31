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


class UsageQuotaResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_response_scope import UsageQuotaResponseScope

        return {
            "enforced": (bool,),
            "org_public_id": (str,),
            "scope": (UsageQuotaResponseScope,),
            "usage_limit": (float,),
        }

    attribute_map = {
        "enforced": "enforced",
        "org_public_id": "org_public_id",
        "scope": "scope",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_,
        enforced: bool,
        org_public_id: str,
        usage_limit: float,
        scope: Union[UsageQuotaResponseScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a usage quota.

        :param enforced: Whether usage above the limit is actively blocked instead of only tracked or alerted on.
        :type enforced: bool

        :param org_public_id: The public ID of the organization that owns the quota.
        :type org_public_id: str

        :param scope: A namespace-specific key and value identifying what the quota applies to within an organization. The object contains exactly one entry. A value of ``"*"`` identifies the default quota applied to entities without a specific quota. This field is omitted for an organization-wide quota.
        :type scope: UsageQuotaResponseScope, optional

        :param usage_limit: The quota limit in the usage units defined by the quota namespace. May be fractional for quotas configured before public writes required whole units.
        :type usage_limit: float
        """
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.enforced = enforced
        self_.org_public_id = org_public_id
        self_.usage_limit = usage_limit
