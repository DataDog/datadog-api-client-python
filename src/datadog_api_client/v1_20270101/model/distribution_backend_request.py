# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DistributionBackendRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: DistributionBackendRequestAnyOfAnyOfItemResponseFormat

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema7, none_type,)}, optional

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

        :param process_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type process_query: ProcessQueryDefinition

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: DistributionBackendRequestAnyOfAnyOfItemQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: DistributionBackendRequestAnyOfAnyOfItemRequestType

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
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of import (
            DistributionBackendRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455761856 import (
            DistributionBackendRequest20270101OneOf4455761856,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455763296 import (
            DistributionBackendRequest20270101OneOf4455763296,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455763936 import (
            DistributionBackendRequest20270101OneOf4455763936,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455764576 import (
            DistributionBackendRequest20270101OneOf4455764576,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455765216 import (
            DistributionBackendRequest20270101OneOf4455765216,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455765856 import (
            DistributionBackendRequest20270101OneOf4455765856,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455766496 import (
            DistributionBackendRequest20270101OneOf4455766496,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455767136 import (
            DistributionBackendRequest20270101OneOf4455767136,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455767776 import (
            DistributionBackendRequest20270101OneOf4455767776,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455768416 import (
            DistributionBackendRequest20270101OneOf4455768416,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455769056 import (
            DistributionBackendRequest20270101OneOf4455769056,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455769696 import (
            DistributionBackendRequest20270101OneOf4455769696,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455770336 import (
            DistributionBackendRequest20270101OneOf4455770336,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455770976 import (
            DistributionBackendRequest20270101OneOf4455770976,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455771616 import (
            DistributionBackendRequest20270101OneOf4455771616,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455772256 import (
            DistributionBackendRequest20270101OneOf4455772256,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455772896 import (
            DistributionBackendRequest20270101OneOf4455772896,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455773536 import (
            DistributionBackendRequest20270101OneOf4455773536,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455774496 import (
            DistributionBackendRequest20270101OneOf4455774496,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455775456 import (
            DistributionBackendRequest20270101OneOf4455775456,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455989472 import (
            DistributionBackendRequest20270101OneOf4455989472,
        )
        from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455990432 import (
            DistributionBackendRequest20270101OneOf4455990432,
        )

        return {
            "oneOf": [
                DistributionBackendRequest20270101OneOf,
                DistributionBackendRequest20270101OneOf4455761856,
                DistributionBackendRequest20270101OneOf4455763296,
                DistributionBackendRequest20270101OneOf4455763936,
                DistributionBackendRequest20270101OneOf4455764576,
                DistributionBackendRequest20270101OneOf4455765216,
                DistributionBackendRequest20270101OneOf4455765856,
                DistributionBackendRequest20270101OneOf4455766496,
                DistributionBackendRequest20270101OneOf4455767136,
                DistributionBackendRequest20270101OneOf4455767776,
                DistributionBackendRequest20270101OneOf4455768416,
                DistributionBackendRequest20270101OneOf4455769056,
                DistributionBackendRequest20270101OneOf4455769696,
                DistributionBackendRequest20270101OneOf4455770336,
                DistributionBackendRequest20270101OneOf4455770976,
                DistributionBackendRequest20270101OneOf4455771616,
                DistributionBackendRequest20270101OneOf4455772256,
                DistributionBackendRequest20270101OneOf4455772896,
                DistributionBackendRequest20270101OneOf4455773536,
                DistributionBackendRequest20270101OneOf4455774496,
                DistributionBackendRequest20270101OneOf4455775456,
                DistributionBackendRequest20270101OneOf4455989472,
                DistributionBackendRequest20270101OneOf4455990432,
            ],
        }
