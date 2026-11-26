# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HeatmapBackendRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: HeatmapBackendRequestAnyOfAnyOfItemResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema5, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param process_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type process_query: ProcessQueryDefinition

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: HeatmapBackendRequestAnyOfAnyOfItemQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: HeatmapBackendRequestAnyOfAnyOfItemRequestType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of import (
            HeatmapBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458138496 import (
            HeatmapBackendRequest20270101OneOf4458138496,
        )
        from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458139936 import (
            HeatmapBackendRequest20270101OneOf4458139936,
        )
        from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458140576 import (
            HeatmapBackendRequest20270101OneOf4458140576,
        )

        return {
            "oneOf": [
                HeatmapBackendRequest20270101OneOf,
                HeatmapBackendRequest20270101OneOf4458138496,
                HeatmapBackendRequest20270101OneOf4458139936,
                HeatmapBackendRequest20270101OneOf4458140576,
            ],
        }
