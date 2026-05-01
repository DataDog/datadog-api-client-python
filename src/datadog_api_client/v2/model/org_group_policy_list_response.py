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
    from datadog_api_client.v2.model.org_group_policy_data import OrgGroupPolicyData
    from datadog_api_client.v2.model.org_group_pagination_links import OrgGroupPaginationLinks
    from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta


class OrgGroupPolicyListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_data import OrgGroupPolicyData
        from datadog_api_client.v2.model.org_group_pagination_links import OrgGroupPaginationLinks
        from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta

        return {
            "data": ([OrgGroupPolicyData],),
            "links": (OrgGroupPaginationLinks,),
            "meta": (OrgGroupPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[OrgGroupPolicyData],
        links: Union[OrgGroupPaginationLinks, UnsetType] = unset,
        meta: Union[OrgGroupPaginationMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of org group policies.

        :param data: An array of org group policies.
        :type data: [OrgGroupPolicyData]

        :param links: Pagination links for navigating between pages of an org group list response.
        :type links: OrgGroupPaginationLinks, optional

        :param meta: Pagination metadata for org group list responses.
        :type meta: OrgGroupPaginationMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
