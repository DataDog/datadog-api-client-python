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
    from datadog_api_client.v2.model.facet_response_data import FacetResponseData
    from datadog_api_client.v2.model.list_facets_response_meta import ListFacetsResponseMeta


class ListFacetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_response_data import FacetResponseData
        from datadog_api_client.v2.model.list_facets_response_meta import ListFacetsResponseMeta

        return {
            "data": ([FacetResponseData],),
            "meta": (ListFacetsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[FacetResponseData], meta: ListFacetsResponseMeta, **kwargs):
        """
        Response containing a list of facets.

        :param data: Array of facets.
        :type data: [FacetResponseData]

        :param meta: Metadata for facets response.
        :type meta: ListFacetsResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
