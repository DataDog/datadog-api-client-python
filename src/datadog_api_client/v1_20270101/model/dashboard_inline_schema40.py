# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DashboardInlineSchema40(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDatasetMetricQueryDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str

        :param byoc_cluster: Test-only generated schema for the dashboard versioning proof of concept.
        :type byoc_cluster: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str], optional

        :param operation_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_mode: str, optional

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str, optional

        :param peer_tags: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_tags: [str], optional

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param resource_hash: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_hash: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str, optional

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str, optional

        :param span_kind: Test-only generated schema for the dashboard versioning proof of concept.
        :type span_kind: SpanKind, optional

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmMetricStat
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
        from datadog_api_client.v1_20270101.model.formula_dataset_metric_query import FormulaDatasetMetricQuery
        from datadog_api_client.v1_20270101.model.formula_dataset_apm_metrics_query import FormulaDatasetApmMetricsQuery

        return {
            "oneOf": [
                FormulaDatasetMetricQuery,
                FormulaDatasetApmMetricsQuery,
            ],
        }
