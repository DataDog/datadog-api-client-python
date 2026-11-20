# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DataProjectionQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param augment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_query: CompositeSourceSubQuery

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: CompositeSourceBaseQuery

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [CompositeCompute]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AggregateAugmentedQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [CompositeGroupBy], optional

        :param join_condition: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_condition: AggregateAugmentedQueryJoinCondition

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str, none_type

        :param dataset_provider: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_provider: PublishedDatasetProvider

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: DatasetListQuerySort, optional
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
        from datadog_api_client.v1_20270101.model.aggregate_augmented_query import AggregateAugmentedQuery
        from datadog_api_client.v1_20270101.model.events_platform_data_projection_query_definition import (
            EventsPlatformDataProjectionQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.dataset_list_query import DatasetListQuery

        return {
            "oneOf": [
                AggregateAugmentedQuery,
                EventsPlatformDataProjectionQueryDefinition,
                DatasetListQuery,
            ],
        }
