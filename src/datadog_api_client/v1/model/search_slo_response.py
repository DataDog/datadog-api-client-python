# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SearchSLOResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.search_slo_response_data import SearchSLOResponseData
        from datadog_api_client.v1.model.search_slo_response_links import SearchSLOResponseLinks
        from datadog_api_client.v1.model.search_slo_response_meta import SearchSLOResponseMeta

        return {
            "data": (SearchSLOResponseData,),
            "links": (SearchSLOResponseLinks,),
            "meta": (SearchSLOResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        A search SLO response containing results from the search query.

        :param data: Data from search SLO response.
        :type data: SearchSLOResponseData, optional

        :param links: Pagination links.
        :type links: SearchSLOResponseLinks, optional

        :param meta: Searches metadata returned by the API.
        :type meta: SearchSLOResponseMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SearchSLOResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
