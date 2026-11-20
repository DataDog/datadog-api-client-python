# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ToplistBackendRequest(ModelComposed):
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
        :type request_type: ToplistBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ToplistBackendRequestAnyOfAnyOfItemResponseFormat

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: ToplistBackendRequest20270101OneOfQuery

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema1, none_type,)}, optional

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

        :param process_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type process_query: ProcessQueryDefinition

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
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of import (
            ToplistBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463319360 import (
            ToplistBackendRequest20270101OneOf4463319360,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463320800 import (
            ToplistBackendRequest20270101OneOf4463320800,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463321920 import (
            ToplistBackendRequest20270101OneOf4463321920,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463323520 import (
            ToplistBackendRequest20270101OneOf4463323520,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463325120 import (
            ToplistBackendRequest20270101OneOf4463325120,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463325920 import (
            ToplistBackendRequest20270101OneOf4463325920,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463326720 import (
            ToplistBackendRequest20270101OneOf4463326720,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463327520 import (
            ToplistBackendRequest20270101OneOf4463327520,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463328320 import (
            ToplistBackendRequest20270101OneOf4463328320,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463329120 import (
            ToplistBackendRequest20270101OneOf4463329120,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463526592 import (
            ToplistBackendRequest20270101OneOf4463526592,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463527392 import (
            ToplistBackendRequest20270101OneOf4463527392,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463528192 import (
            ToplistBackendRequest20270101OneOf4463528192,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463528992 import (
            ToplistBackendRequest20270101OneOf4463528992,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463529792 import (
            ToplistBackendRequest20270101OneOf4463529792,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463530592 import (
            ToplistBackendRequest20270101OneOf4463530592,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463531392 import (
            ToplistBackendRequest20270101OneOf4463531392,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463532192 import (
            ToplistBackendRequest20270101OneOf4463532192,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463532992 import (
            ToplistBackendRequest20270101OneOf4463532992,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463533792 import (
            ToplistBackendRequest20270101OneOf4463533792,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463535232 import (
            ToplistBackendRequest20270101OneOf4463535232,
        )

        return {
            "oneOf": [
                ToplistBackendRequest20270101OneOf,
                ToplistBackendRequest20270101OneOf4463319360,
                ToplistBackendRequest20270101OneOf4463320800,
                ToplistBackendRequest20270101OneOf4463321920,
                ToplistBackendRequest20270101OneOf4463323520,
                ToplistBackendRequest20270101OneOf4463325120,
                ToplistBackendRequest20270101OneOf4463325920,
                ToplistBackendRequest20270101OneOf4463326720,
                ToplistBackendRequest20270101OneOf4463327520,
                ToplistBackendRequest20270101OneOf4463328320,
                ToplistBackendRequest20270101OneOf4463329120,
                ToplistBackendRequest20270101OneOf4463526592,
                ToplistBackendRequest20270101OneOf4463527392,
                ToplistBackendRequest20270101OneOf4463528192,
                ToplistBackendRequest20270101OneOf4463528992,
                ToplistBackendRequest20270101OneOf4463529792,
                ToplistBackendRequest20270101OneOf4463530592,
                ToplistBackendRequest20270101OneOf4463531392,
                ToplistBackendRequest20270101OneOf4463532192,
                ToplistBackendRequest20270101OneOf4463532992,
                ToplistBackendRequest20270101OneOf4463533792,
                ToplistBackendRequest20270101OneOf4463535232,
            ],
        }
