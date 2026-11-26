# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CompositeSourceBaseQuery(ModelComposed):
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

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ListColumn], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [AggregateCompute], optional

        :param compute_count: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute_count: bool, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: CompositeEventsPlatformQueryDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
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
        from datadog_api_client.v1_20270101.model.composite_events_platform_query_definition import (
            CompositeEventsPlatformQueryDefinition,
        )

        return {
            "oneOf": [
                FormulaMetricsQueryMetrics,
                FormulaMetricsQueryCloudCost,
                FormulaMetricsQueryDatadogUsage,
                CompositeEventsPlatformQueryDefinition,
            ],
        }
