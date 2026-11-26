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
    from datadog_api_client.v1_20270101.model.relational_data_query_data_source import RelationalDataQueryDataSource
    from datadog_api_client.v1_20270101.model.relational_data_query_sort import RelationalDataQuerySort


class RelationalDataQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.relational_data_query_data_source import RelationalDataQueryDataSource
        from datadog_api_client.v1_20270101.model.relational_data_query_sort import RelationalDataQuerySort

        return {
            "data_source": (RelationalDataQueryDataSource,),
            "filter": (str,),
            "limit": (float,),
            "sort": (RelationalDataQuerySort,),
            "table_name": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "filter": "filter",
        "limit": "limit",
        "sort": "sort",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        data_source: RelationalDataQueryDataSource,
        table_name: str,
        filter: Union[str, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        sort: Union[RelationalDataQuerySort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: RelationalDataQueryDataSource

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: RelationalDataQuerySort, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.table_name = table_name
