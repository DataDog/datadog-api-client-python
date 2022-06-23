# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SearchSLOResponseDataAttributesFacets(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.search_slo_response_data_attributes_facets_object_string import (
            SearchSLOResponseDataAttributesFacetsObjectString,
        )
        from datadog_api_client.v1.model.search_slo_response_data_attributes_facets_object_int import (
            SearchSLOResponseDataAttributesFacetsObjectInt,
        )

        return {
            "all_tags": ([SearchSLOResponseDataAttributesFacetsObjectString],),
            "creator_name": ([SearchSLOResponseDataAttributesFacetsObjectString],),
            "env_tags": ([SearchSLOResponseDataAttributesFacetsObjectString],),
            "service_tags": ([SearchSLOResponseDataAttributesFacetsObjectString],),
            "slo_type": ([SearchSLOResponseDataAttributesFacetsObjectInt],),
            "target": ([SearchSLOResponseDataAttributesFacetsObjectInt],),
            "team_tags": ([SearchSLOResponseDataAttributesFacetsObjectString],),
            "timeframe": ([SearchSLOResponseDataAttributesFacetsObjectString],),
        }

    attribute_map = {
        "all_tags": "all_tags",
        "creator_name": "creator_name",
        "env_tags": "env_tags",
        "service_tags": "service_tags",
        "slo_type": "slo_type",
        "target": "target",
        "team_tags": "team_tags",
        "timeframe": "timeframe",
    }

    def __init__(self, *args, **kwargs):
        """
        Facets

        :param all_tags: All tags associated with an SLO.
        :type all_tags: [SearchSLOResponseDataAttributesFacetsObjectString], optional

        :param creator_name: Creator of an SLO.
        :type creator_name: [SearchSLOResponseDataAttributesFacetsObjectString], optional

        :param env_tags: Tags with the ``env`` tag key.
        :type env_tags: [SearchSLOResponseDataAttributesFacetsObjectString], optional

        :param service_tags: Tags with the ``service`` tag key.
        :type service_tags: [SearchSLOResponseDataAttributesFacetsObjectString], optional

        :param slo_type: Type of SLO.
        :type slo_type: [SearchSLOResponseDataAttributesFacetsObjectInt], optional

        :param target: SLO Target
        :type target: [SearchSLOResponseDataAttributesFacetsObjectInt], optional

        :param team_tags: Tags with the ``team`` tag key.
        :type team_tags: [SearchSLOResponseDataAttributesFacetsObjectString], optional

        :param timeframe: Timeframes of SLOs.
        :type timeframe: [SearchSLOResponseDataAttributesFacetsObjectString], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SearchSLOResponseDataAttributesFacets, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
