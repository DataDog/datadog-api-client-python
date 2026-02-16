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
    from datadog_api_client.v2.model.connection_data_response import ConnectionDataResponse
    from datadog_api_client.v2.model.list_action_connections_response_meta import ListActionConnectionsResponseMeta


class ListActionConnectionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connection_data_response import ConnectionDataResponse
        from datadog_api_client.v2.model.list_action_connections_response_meta import ListActionConnectionsResponseMeta

        return {
            "data": ([ConnectionDataResponse],),
            "meta": (ListActionConnectionsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ConnectionDataResponse],
        meta: Union[ListActionConnectionsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for listing action connections.

        :param data: An array of action connections.
        :type data: [ConnectionDataResponse]

        :param meta: Metadata for the list connections response.
        :type meta: ListActionConnectionsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
