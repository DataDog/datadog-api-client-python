# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class AdvancedQueryDataset(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetColumn]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AdvancedEventPlatformSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: EventPlatformDatasetDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str

        :param id: Test-only generated schema for the dashboard versioning proof of concept.
        :type id: str

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: MetricDatasetCloudCostScalarAggregation

        :param metric_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric_name: str

        :param tag_names: Test-only generated schema for the dashboard versioning proof of concept.
        :type tag_names: [str], optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [FormulaDatasetFormulasItems]

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [DashboardInlineSchema40]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: FormulaDatasetResponseFormat

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: AnalysisDataset20270101Query

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param sql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type sql_query: str

        :param warehouse: Test-only generated schema for the dashboard versioning proof of concept.
        :type warehouse: str, optional

        :param audience_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type audience_filters: AudienceFilters, optional

        :param conversion_time_ms: Test-only generated schema for the dashboard versioning proof of concept.
        :type conversion_time_ms: float, none_type, optional

        :param entity: Test-only generated schema for the dashboard versioning proof of concept.
        :type entity: ProductAnalyticsJourneyDatasetEntity

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param node_objects: Test-only generated schema for the dashboard versioning proof of concept.
        :type node_objects: {str: (ProductAnalyticsEventQuery,)}

        :param timestamp: Test-only generated schema for the dashboard versioning proof of concept.
        :type timestamp: str
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
        from datadog_api_client.v1_20270101.model.event_platform_dataset_definition import (
            EventPlatformDatasetDefinition,
        )
        from datadog_api_client.v1_20270101.model.referential_dataset_reference_table import (
            ReferentialDatasetReferenceTable,
        )
        from datadog_api_client.v1_20270101.model.referential_dataset_managed_resource import (
            ReferentialDatasetManagedResource,
        )
        from datadog_api_client.v1_20270101.model.actions_datastore_dataset import ActionsDatastoreDataset
        from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar import MetricDatasetCloudCostScalar
        from datadog_api_client.v1_20270101.model.metric_dataset_metric_scalar import MetricDatasetMetricScalar
        from datadog_api_client.v1_20270101.model.formula_dataset import FormulaDataset
        from datadog_api_client.v1_20270101.model.analysis_dataset import AnalysisDataset
        from datadog_api_client.v1_20270101.model.published_analysis import PublishedAnalysis
        from datadog_api_client.v1_20270101.model.snowflake_query_dataset import SnowflakeQueryDataset
        from datadog_api_client.v1_20270101.model.big_query_dataset import BigQueryDataset
        from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset import (
            ProductAnalyticsJourneyDataset,
        )
        from datadog_api_client.v1_20270101.model.historical_discovered_processes_dataset import (
            HistoricalDiscoveredProcessesDataset,
        )

        return {
            "oneOf": [
                EventPlatformDatasetDefinition,
                ReferentialDatasetReferenceTable,
                ReferentialDatasetManagedResource,
                ActionsDatastoreDataset,
                MetricDatasetCloudCostScalar,
                MetricDatasetMetricScalar,
                FormulaDataset,
                AnalysisDataset,
                PublishedAnalysis,
                SnowflakeQueryDataset,
                BigQueryDataset,
                ProductAnalyticsJourneyDataset,
                HistoricalDiscoveredProcessesDataset,
            ],
        }
