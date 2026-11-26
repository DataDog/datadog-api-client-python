# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class FormulaAndFunctionQueryDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param byoc_cluster: Test-only generated schema for the dashboard versioning proof of concept.
        :type byoc_cluster: str, optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaMetricsQueryMetricsDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaAndFunctionEventQueryDefinitionCompute

        :param extractions: Test-only generated schema for the dashboard versioning proof of concept.
        :type extractions: [EventsDataExtraction], optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: FormulaAndFunctionEventQueryGroupByConfig, optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: FormulaAndFunctionEventQueryDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param is_normalized_cpu: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_normalized_cpu: bool, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: QuerySortOrder, optional

        :param tag_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type tag_filters: [str], optional

        :param text_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_filter: str, optional

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param is_upstream: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_upstream: bool, optional

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str

        :param primary_tag_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_value: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmDependencyStat

        :param peer_service: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_service: str, optional

        :param version: Test-only generated schema for the dashboard versioning proof of concept.
        :type version: str, optional

        :param operation_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_mode: str, optional

        :param peer_tags: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_tags: [str], optional

        :param resource_hash: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_hash: str, optional

        :param span_kind: Test-only generated schema for the dashboard versioning proof of concept.
        :type span_kind: SpanKind, optional

        :param additional_query_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type additional_query_filters: str, optional

        :param apply_corrections: Test-only generated schema for the dashboard versioning proof of concept.
        :type apply_corrections: bool, optional

        :param group_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_mode: SloGroupMode

        :param measure: Test-only generated schema for the dashboard versioning proof of concept.
        :type measure: SloMeasure

        :param slo_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_id: str

        :param slo_query_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_query_type: SloQueryType

        :param slo_time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_time_window: SloTimeWindow, optional

        :param exclude_anonymous_traffic: Test-only generated schema for the dashboard versioning proof of concept.
        :type exclude_anonymous_traffic: bool, optional

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: CompositeEventsPlatformQuery

        :param filter_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter_query: CompositeSourceSubQuery

        :param filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type filters: [AggregateFilteredQueryFiltersItems]

        :param augment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_query: CompositeSourceSubQuery

        :param join_condition: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_condition: AggregateAugmentedQueryJoinCondition

        :param segment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type segment_query: AggregateSegmentQuerySegmentQuery

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param dataset_provider: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_provider: PublishedDatasetProvider

        :param time_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_column: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str

        :param computation_scope: Test-only generated schema for the dashboard versioning proof of concept.
        :type computation_scope: ComputationScope, optional

        :param sampling: Test-only generated schema for the dashboard versioning proof of concept.
        :type sampling: FormulaRetentionQuerySampling, optional

        :param anomaly_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type anomaly_options: FormulaDataQualityMetricsQueryAnomalyOptions, optional

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str

        :param scope: Test-only generated schema for the dashboard versioning proof of concept.
        :type scope: str, optional

        :param audience_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type audience_filters: AudienceFilters, optional
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
        from datadog_api_client.v1_20270101.model.formula_metrics_query_metrics import FormulaMetricsQueryMetrics
        from datadog_api_client.v1_20270101.model.formula_metrics_query_cloud_cost import FormulaMetricsQueryCloudCost
        from datadog_api_client.v1_20270101.model.formula_metrics_query_datadog_usage import (
            FormulaMetricsQueryDatadogUsage,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition import (
            FormulaAndFunctionEventQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_process_query_definition import (
            FormulaAndFunctionProcessQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query import (
            FormulaApmDependencyStatsQuery,
        )
        from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query import FormulaApmResourceStatsQuery
        from datadog_api_client.v1_20270101.model.formula_apm_metrics_query import FormulaApmMetricsQuery
        from datadog_api_client.v1_20270101.model.formula_incidents_query import FormulaIncidentsQuery
        from datadog_api_client.v1_20270101.model.formula_slo_query import FormulaSloQuery
        from datadog_api_client.v1_20270101.model.formula_case_query import FormulaCaseQuery
        from datadog_api_client.v1_20270101.model.formula_graph_query import FormulaGraphQuery
        from datadog_api_client.v1_20270101.model.formula_user_journey_query import FormulaUserJourneyQuery
        from datadog_api_client.v1_20270101.model.formula_dora_query import FormulaDoraQuery
        from datadog_api_client.v1_20270101.model.formula_change_tracking_query import FormulaChangeTrackingQuery
        from datadog_api_client.v1_20270101.model.formula_detection_rules_query import FormulaDetectionRulesQuery
        from datadog_api_client.v1_20270101.model.aggregate_filtered_query import AggregateFilteredQuery
        from datadog_api_client.v1_20270101.model.aggregate_augmented_query import AggregateAugmentedQuery
        from datadog_api_client.v1_20270101.model.aggregate_segment_query import AggregateSegmentQuery
        from datadog_api_client.v1_20270101.model.formula_dataset_query import FormulaDatasetQuery
        from datadog_api_client.v1_20270101.model.formula_managed_resource_query import FormulaManagedResourceQuery
        from datadog_api_client.v1_20270101.model.formula_reference_table_query import FormulaReferenceTableQuery
        from datadog_api_client.v1_20270101.model.formula_retention_query import FormulaRetentionQuery
        from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query import (
            FormulaDataQualityMetricsQuery,
        )
        from datadog_api_client.v1_20270101.model.formula_product_analytics_extended_query import (
            FormulaProductAnalyticsExtendedQuery,
        )

        return {
            "oneOf": [
                FormulaMetricsQueryMetrics,
                FormulaMetricsQueryCloudCost,
                FormulaMetricsQueryDatadogUsage,
                FormulaAndFunctionEventQueryDefinition,
                FormulaAndFunctionProcessQueryDefinition,
                FormulaApmDependencyStatsQuery,
                FormulaApmResourceStatsQuery,
                FormulaApmMetricsQuery,
                FormulaIncidentsQuery,
                FormulaSloQuery,
                FormulaCaseQuery,
                FormulaGraphQuery,
                FormulaUserJourneyQuery,
                FormulaDoraQuery,
                FormulaChangeTrackingQuery,
                FormulaDetectionRulesQuery,
                AggregateFilteredQuery,
                AggregateAugmentedQuery,
                AggregateSegmentQuery,
                FormulaDatasetQuery,
                FormulaManagedResourceQuery,
                FormulaReferenceTableQuery,
                FormulaRetentionQuery,
                FormulaDataQualityMetricsQuery,
                FormulaProductAnalyticsExtendedQuery,
            ],
        }
