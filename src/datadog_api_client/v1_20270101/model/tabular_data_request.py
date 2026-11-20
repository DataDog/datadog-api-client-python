# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TabularDataRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TabularAdvancedQueryRequestRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TabularAdvancedQueryRequestResponseFormat

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: TabularLocalDatasetRequest20270101Query
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
        from datadog_api_client.v1_20270101.model.all_list_request_variants import AllListRequestVariants
        from datadog_api_client.v1_20270101.model.tabular_advanced_query_request import TabularAdvancedQueryRequest
        from datadog_api_client.v1_20270101.model.timeseries_formula_request import TimeseriesFormulaRequest
        from datadog_api_client.v1_20270101.model.scalar_formula_request import ScalarFormulaRequest
        from datadog_api_client.v1_20270101.model.tabular_local_dataset_request import TabularLocalDatasetRequest
        from datadog_api_client.v1_20270101.model.histogram_request import HistogramRequest

        return {
            "oneOf": [
                AllListRequestVariants,
                TabularAdvancedQueryRequest,
                TimeseriesFormulaRequest,
                ScalarFormulaRequest,
                TabularLocalDatasetRequest,
                HistogramRequest,
            ],
        }
