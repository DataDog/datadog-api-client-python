# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dataset_list_query_data_source_type import DatasetListQueryDataSourceType
    from datadog_api_client.v1.model.published_dataset_provider import PublishedDatasetProvider
    from datadog_api_client.v1.model.dataset_list_query_sort import DatasetListQuerySort


class DatasetListQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dataset_list_query_data_source_type import DatasetListQueryDataSourceType
        from datadog_api_client.v1.model.published_dataset_provider import PublishedDatasetProvider
        from datadog_api_client.v1.model.dataset_list_query_sort import DatasetListQuerySort

        return {
            "data_source": (DatasetListQueryDataSourceType,),
            "dataset_id": (str,),
            "dataset_provider": (PublishedDatasetProvider,),
            "filter": (str,),
            "limit": (int,),
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
        data_source: DatasetListQueryDataSourceType,
        dataset_id: str,
        dataset_provider: PublishedDatasetProvider,
        filter: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        sort: Union[DatasetListQuerySort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query that lists the rows of a published dataset (a DDSQL query) without aggregation.

        :param data_source: Identifies this as a published-dataset list query.
        :type data_source: DatasetListQueryDataSourceType

        :param dataset_id: ID of the published dataset to query.
        :type dataset_id: str

        :param dataset_provider: Product page that published the dataset queried by a ``DatasetListQuery``. ``ddsql_query`` is the only provider currently supported for host map widgets.
        :type dataset_provider: PublishedDatasetProvider

        :param filter: Filter applied to the dataset's rows, using events-style search syntax.
        :type filter: str, optional

        :param limit: Maximum number of rows to return from the dataset query.
        :type limit: int, optional

        :param sort: Sort configuration for a ``DatasetListQuery``.
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
