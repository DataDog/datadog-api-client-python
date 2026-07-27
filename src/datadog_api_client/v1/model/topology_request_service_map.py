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
    from datadog_api_client.v1.model.topology_query_service_map import TopologyQueryServiceMap
    from datadog_api_client.v1.model.topology_request_type import TopologyRequestType


class TopologyRequestServiceMap(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_query_service_map import TopologyQueryServiceMap
        from datadog_api_client.v1.model.topology_request_type import TopologyRequestType

        return {
            "query": (TopologyQueryServiceMap,),
            "request_type": (TopologyRequestType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        query: Union[TopologyQueryServiceMap, UnsetType] = unset,
        request_type: Union[TopologyRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request that returns nodes and edges from the service map data source.

        :param query: Query to the service map topology data source.
        :type query: TopologyQueryServiceMap, optional

        :param request_type: Widget request type.
        :type request_type: TopologyRequestType, optional
        """
        if query is not unset:
            kwargs["query"] = query
        if request_type is not unset:
            kwargs["request_type"] = request_type
        super().__init__(kwargs)
