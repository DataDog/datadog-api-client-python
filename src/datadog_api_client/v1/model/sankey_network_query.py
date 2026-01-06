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
    from datadog_api_client.v1.model.sankey_network_query_compute import SankeyNetworkQueryCompute
    from datadog_api_client.v1.model.sankey_network_data_source import SankeyNetworkDataSource
    from datadog_api_client.v1.model.sankey_network_query_mode import SankeyNetworkQueryMode
    from datadog_api_client.v1.model.sankey_network_query_sort import SankeyNetworkQuerySort


class SankeyNetworkQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.sankey_network_query_compute import SankeyNetworkQueryCompute
        from datadog_api_client.v1.model.sankey_network_data_source import SankeyNetworkDataSource
        from datadog_api_client.v1.model.sankey_network_query_mode import SankeyNetworkQueryMode
        from datadog_api_client.v1.model.sankey_network_query_sort import SankeyNetworkQuerySort

        return {
            "compute": (SankeyNetworkQueryCompute,),
            "data_source": (SankeyNetworkDataSource,),
            "group_by": ([str],),
            "limit": (int,),
            "mode": (SankeyNetworkQueryMode,),
            "query_string": (str,),
            "should_exclude_missing": (bool,),
            "sort": (SankeyNetworkQuerySort,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "limit": "limit",
        "mode": "mode",
        "query_string": "query_string",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
    }

    def __init__(
        self_,
        data_source: SankeyNetworkDataSource,
        group_by: List[str],
        limit: int,
        query_string: str,
        compute: Union[SankeyNetworkQueryCompute, UnsetType] = unset,
        mode: Union[SankeyNetworkQueryMode, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[SankeyNetworkQuerySort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query configuration for Sankey network widget.

        :param compute: Compute aggregation for network queries.
        :type compute: SankeyNetworkQueryCompute, optional

        :param data_source: Network data source type.
        :type data_source: SankeyNetworkDataSource

        :param group_by: Fields to group by.
        :type group_by: [str]

        :param limit: Maximum number of results.
        :type limit: int

        :param mode: Sankey mode for network queries.
        :type mode: SankeyNetworkQueryMode, optional

        :param query_string: Query string for filtering network data.
        :type query_string: str

        :param should_exclude_missing: Whether to exclude missing values.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for network queries.
        :type sort: SankeyNetworkQuerySort, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if mode is not unset:
            kwargs["mode"] = mode
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.group_by = group_by
        self_.limit = limit
        self_.query_string = query_string
