# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.graph_query_search_filters import GraphQuerySearchFilters
    from datadog_api_client.v1_20270101.model.graph_query_search_join_keys import GraphQuerySearchJoinKeys


class GraphQuerySearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.graph_query_search_filters import GraphQuerySearchFilters
        from datadog_api_client.v1_20270101.model.graph_query_search_join_keys import GraphQuerySearchJoinKeys

        return {
            "expression": (str,),
            "filters": (GraphQuerySearchFilters,),
            "join_keys": (GraphQuerySearchJoinKeys,),
            "nodes": ({str: (str,)},),
        }

    attribute_map = {
        "expression": "expression",
        "filters": "filters",
        "join_keys": "join_keys",
        "nodes": "nodes",
    }

    def __init__(
        self_,
        expression: str,
        nodes: Dict[str, str],
        filters: Union[GraphQuerySearchFilters, UnsetType] = unset,
        join_keys: Union[GraphQuerySearchJoinKeys, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type filters: GraphQuerySearchFilters, optional

        :param join_keys: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_keys: GraphQuerySearchJoinKeys, optional

        :param nodes: Test-only generated schema for the dashboard versioning proof of concept.
        :type nodes: {str: (str,)}
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        super().__init__(kwargs)

        self_.expression = expression
        self_.nodes = nodes
