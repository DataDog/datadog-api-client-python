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
    from datadog_api_client.v2.model.org_group_data import OrgGroupData
    from datadog_api_client.v2.model.org_group_membership_data import OrgGroupMembershipData
    from datadog_api_client.v2.model.org_group_pagination_links import OrgGroupPaginationLinks
    from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta


class OrgGroupListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_data import OrgGroupData
        from datadog_api_client.v2.model.org_group_membership_data import OrgGroupMembershipData
        from datadog_api_client.v2.model.org_group_pagination_links import OrgGroupPaginationLinks
        from datadog_api_client.v2.model.org_group_pagination_meta import OrgGroupPaginationMeta

        return {
            "data": ([OrgGroupData],),
            "included": ([OrgGroupMembershipData],),
            "links": (OrgGroupPaginationLinks,),
            "meta": (OrgGroupPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[OrgGroupData],
        included: Union[List[OrgGroupMembershipData], UnsetType] = unset,
        links: Union[OrgGroupPaginationLinks, UnsetType] = unset,
        meta: Union[OrgGroupPaginationMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of org groups.

        :param data: An array of org groups.
        :type data: [OrgGroupData]

        :param included: Related resources included in the response when requested with the ``include`` parameter.
        :type included: [OrgGroupMembershipData], optional

        :param links: Pagination links for navigating between pages of an org group list response.
        :type links: OrgGroupPaginationLinks, optional

        :param meta: Pagination metadata for org group list responses.
        :type meta: OrgGroupPaginationMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
