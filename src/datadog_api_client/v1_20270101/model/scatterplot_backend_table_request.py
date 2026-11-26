# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ScatterplotBackendTableRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: ScatterplotBackendTableRequest20270101OneOfQuery

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema2, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [ScatterplotFormula]

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional
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
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of import (
            ScatterplotBackendTableRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461521920 import (
            ScatterplotBackendTableRequest20270101OneOf4461521920,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461523200 import (
            ScatterplotBackendTableRequest20270101OneOf4461523200,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461524480 import (
            ScatterplotBackendTableRequest20270101OneOf4461524480,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461525600 import (
            ScatterplotBackendTableRequest20270101OneOf4461525600,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461756480 import (
            ScatterplotBackendTableRequest20270101OneOf4461756480,
        )

        return {
            "oneOf": [
                ScatterplotBackendTableRequest20270101OneOf,
                ScatterplotBackendTableRequest20270101OneOf4461521920,
                ScatterplotBackendTableRequest20270101OneOf4461523200,
                ScatterplotBackendTableRequest20270101OneOf4461524480,
                ScatterplotBackendTableRequest20270101OneOf4461525600,
                ScatterplotBackendTableRequest20270101OneOf4461756480,
            ],
        }
