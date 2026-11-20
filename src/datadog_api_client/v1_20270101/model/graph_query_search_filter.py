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
    from datadog_api_client.v1_20270101.model.graph_query_search_filter_operator import GraphQuerySearchFilterOperator
    from datadog_api_client.v1_20270101.model.graph_target import GraphTarget
    from datadog_api_client.v1_20270101.model.graph_target_node import GraphTargetNode
    from datadog_api_client.v1_20270101.model.graph_target_path import GraphTargetPath


class GraphQuerySearchFilter(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.graph_query_search_filter_operator import (
            GraphQuerySearchFilterOperator,
        )
        from datadog_api_client.v1_20270101.model.graph_target import GraphTarget

        return {
            "name": (str,),
            "operator": (GraphQuerySearchFilterOperator,),
            "target": (GraphTarget,),
            "value": (float,),
        }

    attribute_map = {
        "name": "name",
        "operator": "operator",
        "target": "target",
        "value": "value",
    }

    def __init__(
        self_,
        name: str,
        operator: GraphQuerySearchFilterOperator,
        value: float,
        target: Union[GraphTarget, GraphTargetNode, GraphTargetPath, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param operator: Test-only generated schema for the dashboard versioning proof of concept.
        :type operator: GraphQuerySearchFilterOperator

        :param target: Test-only generated schema for the dashboard versioning proof of concept.
        :type target: GraphTarget, optional

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: float
        """
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.name = name
        self_.operator = operator
        self_.value = value
