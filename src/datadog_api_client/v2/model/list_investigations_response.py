# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_investigations_response_data import ListInvestigationsResponseData
    from datadog_api_client.v2.model.list_investigations_response_links import ListInvestigationsResponseLinks
    from datadog_api_client.v2.model.list_investigations_response_meta import ListInvestigationsResponseMeta


class ListInvestigationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_investigations_response_data import ListInvestigationsResponseData
        from datadog_api_client.v2.model.list_investigations_response_links import ListInvestigationsResponseLinks
        from datadog_api_client.v2.model.list_investigations_response_meta import ListInvestigationsResponseMeta

        return {
            "data": ([ListInvestigationsResponseData],),
            "links": (ListInvestigationsResponseLinks,),
            "meta": (ListInvestigationsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ListInvestigationsResponseData],
        links: ListInvestigationsResponseLinks,
        meta: ListInvestigationsResponseMeta,
        **kwargs,
    ):
        """
        Response for listing investigations.

        :param data: List of investigations.
        :type data: [ListInvestigationsResponseData]

        :param links: Pagination links for the list investigations response.
        :type links: ListInvestigationsResponseLinks

        :param meta: Metadata for the list investigations response.
        :type meta: ListInvestigationsResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
        self_.meta = meta
