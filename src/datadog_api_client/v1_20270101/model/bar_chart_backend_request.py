# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class BarChartBackendRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: BarChartBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: BarChartBackendRequestAnyOfAnyOfItemResponseFormat

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: BarChartBackendRequest20270101OneOfQuery
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
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request20270101_one_of import (
            BarChartBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request20270101_one_of4454434112 import (
            BarChartBackendRequest20270101OneOf4454434112,
        )
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request20270101_one_of4454435552 import (
            BarChartBackendRequest20270101OneOf4454435552,
        )
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request20270101_one_of4454436672 import (
            BarChartBackendRequest20270101OneOf4454436672,
        )
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request20270101_one_of4454438272 import (
            BarChartBackendRequest20270101OneOf4454438272,
        )

        return {
            "oneOf": [
                BarChartBackendRequest20270101OneOf,
                BarChartBackendRequest20270101OneOf4454434112,
                BarChartBackendRequest20270101OneOf4454435552,
                BarChartBackendRequest20270101OneOf4454436672,
                BarChartBackendRequest20270101OneOf4454438272,
            ],
        }
