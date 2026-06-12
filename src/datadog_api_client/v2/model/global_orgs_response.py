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
    from datadog_api_client.v2.model.global_org_data import GlobalOrgData
    from datadog_api_client.v2.model.global_orgs_links import GlobalOrgsLinks
    from datadog_api_client.v2.model.global_orgs_meta import GlobalOrgsMeta


class GlobalOrgsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_org_data import GlobalOrgData
        from datadog_api_client.v2.model.global_orgs_links import GlobalOrgsLinks
        from datadog_api_client.v2.model.global_orgs_meta import GlobalOrgsMeta

        return {
            "data": ([GlobalOrgData],),
            "links": (GlobalOrgsLinks,),
            "meta": (GlobalOrgsMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[GlobalOrgData],
        links: Union[GlobalOrgsLinks, UnsetType] = unset,
        meta: Union[GlobalOrgsMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing organizations across regions for the authenticated user.

        :param data: Organizations across regions for the authenticated user.
        :type data: [GlobalOrgData]

        :param links: Pagination links.
        :type links: GlobalOrgsLinks, optional

        :param meta: Response metadata object.
        :type meta: GlobalOrgsMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
