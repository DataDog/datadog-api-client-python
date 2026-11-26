# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DatasetListRequest20270101Query(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: DatasetListQueryDataSource

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

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
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
        from datadog_api_client.v1.model.dataset_list_query import DatasetListQuery
        from datadog_api_client.v1.model.relational_data_query import RelationalDataQuery

        return {
            "oneOf": [
                DatasetListQuery,
                RelationalDataQuery,
            ],
        }
