# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of_query import (
        ScatterplotBackendTableRequest20270101OneOfQuery,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type4451204320 import (
        ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451204320,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_response_format4451204640 import (
        ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451204640,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
    from datadog_api_client.v1_20270101.model.tree_data_projection_bar_chart import TreeDataProjectionBarChart
    from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst import TreeDataProjectionSunburst
    from datadog_api_client.v1_20270101.model.tree_data_projection_toplist import TreeDataProjectionToplist
    from datadog_api_client.v1_20270101.model.tree_data_projection_treemap import TreeDataProjectionTreemap
    from datadog_api_client.v1_20270101.model.query_value_projection import QueryValueProjection
    from datadog_api_client.v1_20270101.model.query_table_projection import QueryTableProjection
    from datadog_api_client.v1_20270101.model.run_chart_projection import RunChartProjection
    from datadog_api_client.v1_20270101.model.structured_analysis_query import StructuredAnalysisQuery
    from datadog_api_client.v1_20270101.model.sampled_analysis_query import SampledAnalysisQuery


class ScatterplotBackendTableRequest20270101OneOf4461521920(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of_query import (
            ScatterplotBackendTableRequest20270101OneOfQuery,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type4451204320 import (
            ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451204320,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_response_format4451204640 import (
            ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451204640,
        )

        return {
            "projection": (TabularProjection,),
            "query": (ScatterplotBackendTableRequest20270101OneOfQuery,),
            "request_type": (ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451204320,),
            "response_format": (ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451204640,),
        }

    attribute_map = {
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        query: Union[ScatterplotBackendTableRequest20270101OneOfQuery, StructuredAnalysisQuery, SampledAnalysisQuery],
        request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451204320,
        response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451204640,
        projection: Union[
            TabularProjection,
            ScatterplotProjection,
            TreeDataProjectionBarChart,
            TreeDataProjectionSunburst,
            TreeDataProjectionToplist,
            TreeDataProjectionTreemap,
            QueryValueProjection,
            QueryTableProjection,
            RunChartProjection,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: ScatterplotBackendTableRequest20270101OneOfQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451204320

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451204640
        """
        if projection is not unset:
            kwargs["projection"] = projection
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
        self_.response_format = response_format
