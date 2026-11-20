# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SunburstBackendRequest(ModelComposed):
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
        :type request_type: SunburstBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: SunburstBackendRequestAnyOfAnyOfItemResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: SunburstRequestStyle, optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: SunburstBackendRequest20270101OneOfQuery
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
        from datadog_api_client.v1_20270101.model.sunburst_backend_request20270101_one_of import (
            SunburstBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.sunburst_backend_request20270101_one_of4462422560 import (
            SunburstBackendRequest20270101OneOf4462422560,
        )
        from datadog_api_client.v1_20270101.model.sunburst_backend_request20270101_one_of4462423840 import (
            SunburstBackendRequest20270101OneOf4462423840,
        )
        from datadog_api_client.v1_20270101.model.sunburst_backend_request20270101_one_of4462424800 import (
            SunburstBackendRequest20270101OneOf4462424800,
        )

        return {
            "oneOf": [
                SunburstBackendRequest20270101OneOf,
                SunburstBackendRequest20270101OneOf4462422560,
                SunburstBackendRequest20270101OneOf4462423840,
                SunburstBackendRequest20270101OneOf4462424800,
            ],
        }
