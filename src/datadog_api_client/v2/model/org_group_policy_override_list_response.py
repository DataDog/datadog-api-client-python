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
    from datadog_api_client.v2.model.org_group_policy_override_data import OrgGroupPolicyOverrideData
    from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta


class OrgGroupPolicyOverrideListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_data import OrgGroupPolicyOverrideData
        from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta

        return {
            "data": ([OrgGroupPolicyOverrideData],),
            "meta": (OrgGroupPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[OrgGroupPolicyOverrideData], meta: Union[OrgGroupPaginationMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a list of org group policy overrides.

        :param data: An array of org group policy overrides.
        :type data: [OrgGroupPolicyOverrideData]

        :param meta: Pagination metadata.
        :type meta: OrgGroupPaginationMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
