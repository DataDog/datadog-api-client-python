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
    from datadog_api_client.v1.model.retention_compute import RetentionCompute
    from datadog_api_client.v1.model.retention_data_source import RetentionDataSource
    from datadog_api_client.v1.model.retention_filters import RetentionFilters
    from datadog_api_client.v1.model.retention_group_by import RetentionGroupBy
    from datadog_api_client.v1.model.retention_search import RetentionSearch


class RetentionQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_compute import RetentionCompute
        from datadog_api_client.v1.model.retention_data_source import RetentionDataSource
        from datadog_api_client.v1.model.retention_filters import RetentionFilters
        from datadog_api_client.v1.model.retention_group_by import RetentionGroupBy
        from datadog_api_client.v1.model.retention_search import RetentionSearch

        return {
            "compute": (RetentionCompute,),
            "data_source": (RetentionDataSource,),
            "filters": (RetentionFilters,),
            "group_by": ([RetentionGroupBy],),
            "name": (str,),
            "search": (RetentionSearch,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "filters": "filters",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
    }

    def __init__(
        self_,
        compute: RetentionCompute,
        data_source: RetentionDataSource,
        search: RetentionSearch,
        filters: Union[RetentionFilters, UnsetType] = unset,
        group_by: Union[List[RetentionGroupBy], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Retention query definition.

        :param compute: Compute configuration for retention queries.
        :type compute: RetentionCompute

        :param data_source: Data source for retention queries.
        :type data_source: RetentionDataSource

        :param filters: Filters for retention queries.
        :type filters: RetentionFilters, optional

        :param group_by: Group by configuration.
        :type group_by: [RetentionGroupBy], optional

        :param name: Name of the query.
        :type name: str, optional

        :param search: Search configuration for retention queries.
        :type search: RetentionSearch
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.search = search
