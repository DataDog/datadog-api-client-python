# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dataset_list_query_data_source import DatasetListQueryDataSource
    from datadog_api_client.v1_20270101.model.published_dataset_provider import PublishedDatasetProvider
    from datadog_api_client.v1_20270101.model.dataset_list_query_sort import DatasetListQuerySort


class DatasetListQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_list_query_data_source import DatasetListQueryDataSource
        from datadog_api_client.v1_20270101.model.published_dataset_provider import PublishedDatasetProvider
        from datadog_api_client.v1_20270101.model.dataset_list_query_sort import DatasetListQuerySort

        return {
            "data_source": (DatasetListQueryDataSource,),
            "dataset_id": (str, none_type),
            "dataset_provider": (PublishedDatasetProvider,),
            "filter": (str,),
            "limit": (float,),
            "sort": (DatasetListQuerySort,),
        }

    attribute_map = {
        "data_source": "data_source",
        "dataset_id": "dataset_id",
        "dataset_provider": "dataset_provider",
        "filter": "filter",
        "limit": "limit",
        "sort": "sort",
    }

    def __init__(
        self_,
        data_source: DatasetListQueryDataSource,
        dataset_id: Union[str, none_type],
        dataset_provider: PublishedDatasetProvider,
        filter: Union[str, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        sort: Union[DatasetListQuerySort, UnsetType] = unset,
        **kwargs,
    ):
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
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.dataset_id = dataset_id
        self_.dataset_provider = dataset_provider
