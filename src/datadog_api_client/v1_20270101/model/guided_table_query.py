# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GuidedTableQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: MetricsLikeQueryFragmentMetricsDataSource

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param metric_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric_name: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: EventsQueryFragmentDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param byoc_cluster: Test-only generated schema for the dashboard versioning proof of concept.
        :type byoc_cluster: str, optional

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
        from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_metrics import (
            MetricsLikeQueryFragmentMetrics,
        )
        from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_cloud_cost import (
            MetricsLikeQueryFragmentCloudCost,
        )
        from datadog_api_client.v1_20270101.model.events_query_fragment_definition import EventsQueryFragmentDefinition
        from datadog_api_client.v1_20270101.model.referential_query_fragment_reference_table import (
            ReferentialQueryFragmentReferenceTable,
        )
        from datadog_api_client.v1_20270101.model.referential_query_fragment_managed_resource import (
            ReferentialQueryFragmentManagedResource,
        )
        from datadog_api_client.v1_20270101.model.published_analysis_query_fragment import (
            PublishedAnalysisQueryFragment,
        )
        from datadog_api_client.v1_20270101.model.apm_metrics_query_fragment import ApmMetricsQueryFragment

        return {
            "oneOf": [
                MetricsLikeQueryFragmentMetrics,
                MetricsLikeQueryFragmentCloudCost,
                EventsQueryFragmentDefinition,
                ReferentialQueryFragmentReferenceTable,
                ReferentialQueryFragmentManagedResource,
                PublishedAnalysisQueryFragment,
                ApmMetricsQueryFragment,
            ],
        }
