# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class QueryTableBackendRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: [CellDisplayModeOption], optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [[TextFormattingRule]], optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: QueryTableBackendRequest20270101OneOfQuery

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema4, none_type,)}, optional

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

        :param apm_stats_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type apm_stats_query: ApmStatsQuery

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [TableColumn]

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [GuidedTableQuery]

        :param rows: Test-only generated schema for the dashboard versioning proof of concept.
        :type rows: TableRows

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [TableFormula], optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

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
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of import (
            QueryTableBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459913248 import (
            QueryTableBackendRequest20270101OneOf4459913248,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459916288 import (
            QueryTableBackendRequest20270101OneOf4459916288,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459919328 import (
            QueryTableBackendRequest20270101OneOf4459919328,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460101856 import (
            QueryTableBackendRequest20270101OneOf4460101856,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460104096 import (
            QueryTableBackendRequest20270101OneOf4460104096,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460106336 import (
            QueryTableBackendRequest20270101OneOf4460106336,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460108576 import (
            QueryTableBackendRequest20270101OneOf4460108576,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460110816 import (
            QueryTableBackendRequest20270101OneOf4460110816,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460113056 import (
            QueryTableBackendRequest20270101OneOf4460113056,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460115296 import (
            QueryTableBackendRequest20270101OneOf4460115296,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460117536 import (
            QueryTableBackendRequest20270101OneOf4460117536,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460300064 import (
            QueryTableBackendRequest20270101OneOf4460300064,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460302304 import (
            QueryTableBackendRequest20270101OneOf4460302304,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460304544 import (
            QueryTableBackendRequest20270101OneOf4460304544,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460306784 import (
            QueryTableBackendRequest20270101OneOf4460306784,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460309024 import (
            QueryTableBackendRequest20270101OneOf4460309024,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460311264 import (
            QueryTableBackendRequest20270101OneOf4460311264,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460313504 import (
            QueryTableBackendRequest20270101OneOf4460313504,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460513216 import (
            QueryTableBackendRequest20270101OneOf4460513216,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460516096 import (
            QueryTableBackendRequest20270101OneOf4460516096,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460519136 import (
            QueryTableBackendRequest20270101OneOf4460519136,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460522016 import (
            QueryTableBackendRequest20270101OneOf4460522016,
        )

        return {
            "oneOf": [
                QueryTableBackendRequest20270101OneOf,
                QueryTableBackendRequest20270101OneOf4459913248,
                QueryTableBackendRequest20270101OneOf4459916288,
                QueryTableBackendRequest20270101OneOf4459919328,
                QueryTableBackendRequest20270101OneOf4460101856,
                QueryTableBackendRequest20270101OneOf4460104096,
                QueryTableBackendRequest20270101OneOf4460106336,
                QueryTableBackendRequest20270101OneOf4460108576,
                QueryTableBackendRequest20270101OneOf4460110816,
                QueryTableBackendRequest20270101OneOf4460113056,
                QueryTableBackendRequest20270101OneOf4460115296,
                QueryTableBackendRequest20270101OneOf4460117536,
                QueryTableBackendRequest20270101OneOf4460300064,
                QueryTableBackendRequest20270101OneOf4460302304,
                QueryTableBackendRequest20270101OneOf4460304544,
                QueryTableBackendRequest20270101OneOf4460306784,
                QueryTableBackendRequest20270101OneOf4460309024,
                QueryTableBackendRequest20270101OneOf4460311264,
                QueryTableBackendRequest20270101OneOf4460313504,
                QueryTableBackendRequest20270101OneOf4460513216,
                QueryTableBackendRequest20270101OneOf4460516096,
                QueryTableBackendRequest20270101OneOf4460519136,
                QueryTableBackendRequest20270101OneOf4460522016,
            ],
        }
