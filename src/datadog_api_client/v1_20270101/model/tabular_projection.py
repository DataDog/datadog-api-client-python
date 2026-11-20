# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TabularProjection(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [ScatterplotProjectionDimensionsItems]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ScatterplotProjectionType

        :param group_styles: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_styles: [GroupStyleRule], optional

        :param column_order: Test-only generated schema for the dashboard versioning proof of concept.
        :type column_order: QueryTableProjectionColumnOrder, optional

        :param unlisted_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type unlisted_columns: QueryTableProjectionUnlistedColumns, optional
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
        from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
        from datadog_api_client.v1_20270101.model.tree_data_projection_bar_chart import TreeDataProjectionBarChart
        from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst import TreeDataProjectionSunburst
        from datadog_api_client.v1_20270101.model.tree_data_projection_toplist import TreeDataProjectionToplist
        from datadog_api_client.v1_20270101.model.tree_data_projection_treemap import TreeDataProjectionTreemap
        from datadog_api_client.v1_20270101.model.query_value_projection import QueryValueProjection
        from datadog_api_client.v1_20270101.model.query_table_projection import QueryTableProjection
        from datadog_api_client.v1_20270101.model.run_chart_projection import RunChartProjection

        return {
            "oneOf": [
                ScatterplotProjection,
                TreeDataProjectionBarChart,
                TreeDataProjectionSunburst,
                TreeDataProjectionToplist,
                TreeDataProjectionTreemap,
                QueryValueProjection,
                QueryTableProjection,
                RunChartProjection,
            ],
        }
