# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class QueryValueBackendRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: ComparisonRequest, optional

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
        :type request_type: QueryValueBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryValueBackendRequestAnyOfAnyOfItemResponseFormat

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema3, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param log_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type log_query: LogQueryDefinition

        :param apm_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type apm_query: LogQueryDefinition

        :param network_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type network_query: LogQueryDefinition

        :param rum_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type rum_query: LogQueryDefinition

        :param security_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type security_query: LogQueryDefinition

        :param compliance_findings_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type compliance_findings_query: LogQueryDefinition

        :param event_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type event_query: LogQueryDefinition

        :param profile_metrics_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type profile_metrics_query: LogQueryDefinition

        :param ci_pipeline_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ci_pipeline_query: LogQueryDefinition

        :param ci_test_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ci_test_query: LogQueryDefinition

        :param audit_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type audit_query: LogQueryDefinition

        :param appsecspan_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type appsecspan_query: LogQueryDefinition

        :param synthetics_batches: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_batches: LogQueryDefinition

        :param synthetics_test_runs: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_test_runs: LogQueryDefinition

        :param profilemetrics_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type profilemetrics_query: LogQueryDefinition
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
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of import (
            QueryValueBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460683296 import (
            QueryValueBackendRequest20270101OneOf4460683296,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460685056 import (
            QueryValueBackendRequest20270101OneOf4460685056,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460686496 import (
            QueryValueBackendRequest20270101OneOf4460686496,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460688416 import (
            QueryValueBackendRequest20270101OneOf4460688416,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460689536 import (
            QueryValueBackendRequest20270101OneOf4460689536,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460690656 import (
            QueryValueBackendRequest20270101OneOf4460690656,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460904832 import (
            QueryValueBackendRequest20270101OneOf4460904832,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460905952 import (
            QueryValueBackendRequest20270101OneOf4460905952,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460907072 import (
            QueryValueBackendRequest20270101OneOf4460907072,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460908192 import (
            QueryValueBackendRequest20270101OneOf4460908192,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460909312 import (
            QueryValueBackendRequest20270101OneOf4460909312,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460910432 import (
            QueryValueBackendRequest20270101OneOf4460910432,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460911552 import (
            QueryValueBackendRequest20270101OneOf4460911552,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460912672 import (
            QueryValueBackendRequest20270101OneOf4460912672,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460913792 import (
            QueryValueBackendRequest20270101OneOf4460913792,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460914912 import (
            QueryValueBackendRequest20270101OneOf4460914912,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460916032 import (
            QueryValueBackendRequest20270101OneOf4460916032,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460917152 import (
            QueryValueBackendRequest20270101OneOf4460917152,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460918912 import (
            QueryValueBackendRequest20270101OneOf4460918912,
        )

        return {
            "oneOf": [
                QueryValueBackendRequest20270101OneOf,
                QueryValueBackendRequest20270101OneOf4460683296,
                QueryValueBackendRequest20270101OneOf4460685056,
                QueryValueBackendRequest20270101OneOf4460686496,
                QueryValueBackendRequest20270101OneOf4460688416,
                QueryValueBackendRequest20270101OneOf4460689536,
                QueryValueBackendRequest20270101OneOf4460690656,
                QueryValueBackendRequest20270101OneOf4460904832,
                QueryValueBackendRequest20270101OneOf4460905952,
                QueryValueBackendRequest20270101OneOf4460907072,
                QueryValueBackendRequest20270101OneOf4460908192,
                QueryValueBackendRequest20270101OneOf4460909312,
                QueryValueBackendRequest20270101OneOf4460910432,
                QueryValueBackendRequest20270101OneOf4460911552,
                QueryValueBackendRequest20270101OneOf4460912672,
                QueryValueBackendRequest20270101OneOf4460913792,
                QueryValueBackendRequest20270101OneOf4460914912,
                QueryValueBackendRequest20270101OneOf4460916032,
                QueryValueBackendRequest20270101OneOf4460917152,
                QueryValueBackendRequest20270101OneOf4460918912,
            ],
        }
