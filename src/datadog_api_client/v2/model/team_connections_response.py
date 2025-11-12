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
    from datadog_api_client.v2.model.team_connection import TeamConnection
    from datadog_api_client.v2.model.connections_response_meta import ConnectionsResponseMeta


class TeamConnectionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_connection import TeamConnection
        from datadog_api_client.v2.model.connections_response_meta import ConnectionsResponseMeta

        return {
            "data": ([TeamConnection],),
            "meta": (ConnectionsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[TeamConnection], UnsetType] = unset,
        meta: Union[ConnectionsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing information about multiple team connections.

        :param data: Array of team connections.
        :type data: [TeamConnection], optional

        :param meta: Connections response metadata.
        :type meta: ConnectionsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
