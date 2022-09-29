# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SearchSLOResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.search_slo_response_data_attributes_facets import (
            SearchSLOResponseDataAttributesFacets,
        )
        from datadog_api_client.v1.model.search_service_level_objective import SearchServiceLevelObjective

        return {
            "facets": (SearchSLOResponseDataAttributesFacets,),
            "slos": ([SearchServiceLevelObjective],),
        }

    attribute_map = {
        "facets": "facets",
        "slos": "slos",
    }

    def __init__(self_, *args, **kwargs):
        """
        Attributes

        :param facets: Facets
        :type facets: SearchSLOResponseDataAttributesFacets, optional

        :param slos: SLOs
        :type slos: [SearchServiceLevelObjective], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
