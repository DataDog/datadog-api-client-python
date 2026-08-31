# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageQuotaRequestScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

    def __init__(self_, **kwargs):
        """
        A namespace-specific key and value identifying what the quota applies to within an organization. The object must contain exactly one entry. Use ``"*"`` as the value for the default quota applied to entities without a specific quota, or omit the scope for an organization-wide quota. A specific value must identify an existing user handle in the caller's organization when ``include_descendants`` is false. When ``include_descendants`` is true, the handle must exist in the caller's organization or in at least one targeted descendant organization; the quota is then applied only to the organizations where that handle exists, and the request fails only if the handle exists in none of them.
        """
        super().__init__(kwargs)
