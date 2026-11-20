# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TimeseriesWidgetRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: WidgetDisplayType, optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param metadata: Test-only generated schema for the dashboard versioning proof of concept.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TimeseriesWidgetFormulaRequestResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TimeseriesRequestStyle, optional

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema50, none_type,)}, optional

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

        :param legacy_event_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type legacy_event_query: LegacyEventManagementQuery

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TimeseriesWidgetDdsqlRequestRequestType

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TimeseriesProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: StructuredAnalysisQuery
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
        from datadog_api_client.v1_20270101.model.timeseries_widget_formula_request import (
            TimeseriesWidgetFormulaRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_metric_request import TimeseriesWidgetMetricRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_log_request import TimeseriesWidgetLogRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_apm_request import TimeseriesWidgetApmRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_network_request import (
            TimeseriesWidgetNetworkRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_rum_request import TimeseriesWidgetRumRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_security_request import (
            TimeseriesWidgetSecurityRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_compliance_findings_request import (
            TimeseriesWidgetComplianceFindingsRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_event_request import TimeseriesWidgetEventRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_profiling_metrics_request import (
            TimeseriesWidgetProfilingMetricsRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_ci_pipeline_request import (
            TimeseriesWidgetCiPipelineRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_ci_test_request import TimeseriesWidgetCiTestRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_audit_request import TimeseriesWidgetAuditRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_appsec_span_request import (
            TimeseriesWidgetAppsecSpanRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_synthetics_batches_request import (
            TimeseriesWidgetSyntheticsBatchesRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_synthetics_test_runs_request import (
            TimeseriesWidgetSyntheticsTestRunsRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_process_request import (
            TimeseriesWidgetProcessRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_legacy_profile_metrics_request import (
            TimeseriesWidgetLegacyProfileMetricsRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_legacy_event_request import (
            TimeseriesWidgetLegacyEventRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request import TimeseriesWidgetDdsqlRequest
        from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request import (
            TimeseriesWidgetAdvancedQueryRequest,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_local_dataset_request import (
            TimeseriesWidgetLocalDatasetRequest,
        )

        return {
            "oneOf": [
                TimeseriesWidgetFormulaRequest,
                TimeseriesWidgetMetricRequest,
                TimeseriesWidgetLogRequest,
                TimeseriesWidgetApmRequest,
                TimeseriesWidgetNetworkRequest,
                TimeseriesWidgetRumRequest,
                TimeseriesWidgetSecurityRequest,
                TimeseriesWidgetComplianceFindingsRequest,
                TimeseriesWidgetEventRequest,
                TimeseriesWidgetProfilingMetricsRequest,
                TimeseriesWidgetCiPipelineRequest,
                TimeseriesWidgetCiTestRequest,
                TimeseriesWidgetAuditRequest,
                TimeseriesWidgetAppsecSpanRequest,
                TimeseriesWidgetSyntheticsBatchesRequest,
                TimeseriesWidgetSyntheticsTestRunsRequest,
                TimeseriesWidgetProcessRequest,
                TimeseriesWidgetLegacyProfileMetricsRequest,
                TimeseriesWidgetLegacyEventRequest,
                TimeseriesWidgetDdsqlRequest,
                TimeseriesWidgetAdvancedQueryRequest,
                TimeseriesWidgetLocalDatasetRequest,
            ],
        }
