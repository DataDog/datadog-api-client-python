# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dataset_compute import DatasetCompute
    from datadog_api_client.v1_20270101.model.formula_dataset_query_data_source import FormulaDatasetQueryDataSource
    from datadog_api_client.v1_20270101.model.published_dataset_provider import PublishedDatasetProvider
    from datadog_api_client.v1_20270101.model.dataset_group_by import DatasetGroupBy
    from datadog_api_client.v1_20270101.model.dataset_sort import DatasetSort


class FormulaDatasetQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_compute import DatasetCompute
        from datadog_api_client.v1_20270101.model.formula_dataset_query_data_source import FormulaDatasetQueryDataSource
        from datadog_api_client.v1_20270101.model.published_dataset_provider import PublishedDatasetProvider
        from datadog_api_client.v1_20270101.model.dataset_group_by import DatasetGroupBy
        from datadog_api_client.v1_20270101.model.dataset_sort import DatasetSort

        return {
            "compute": ([DatasetCompute],),
            "data_source": (FormulaDatasetQueryDataSource,),
            "dataset_id": (str,),
            "dataset_provider": (PublishedDatasetProvider,),
            "group_by": ([DatasetGroupBy],),
            "limit": (float,),
            "name": (str,),
            "query_filter": (str,),
            "sort": ([DatasetSort],),
            "time_column": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "dataset_id": "dataset_id",
        "dataset_provider": "dataset_provider",
        "group_by": "group_by",
        "limit": "limit",
        "name": "name",
        "query_filter": "query_filter",
        "sort": "sort",
        "time_column": "time_column",
    }

    def __init__(
        self_,
        compute: List[DatasetCompute],
        data_source: FormulaDatasetQueryDataSource,
        dataset_id: str,
        dataset_provider: PublishedDatasetProvider,
        name: str,
        group_by: Union[List[DatasetGroupBy], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        sort: Union[List[DatasetSort], UnsetType] = unset,
        time_column: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [DatasetCompute]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDatasetQueryDataSource

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param dataset_provider: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_provider: PublishedDatasetProvider

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [DatasetGroupBy], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: [DatasetSort], optional

        :param time_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_column: str, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if sort is not unset:
            kwargs["sort"] = sort
        if time_column is not unset:
            kwargs["time_column"] = time_column
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.dataset_id = dataset_id
        self_.dataset_provider = dataset_provider
        self_.name = name
