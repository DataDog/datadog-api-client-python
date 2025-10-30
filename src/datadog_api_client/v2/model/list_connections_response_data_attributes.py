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
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items import (
        ListConnectionsResponseDataAttributesConnectionsItems,
    )


class ListConnectionsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items import (
            ListConnectionsResponseDataAttributesConnectionsItems,
        )

        return {
            "connections": ([ListConnectionsResponseDataAttributesConnectionsItems],),
        }

    attribute_map = {
        "connections": "connections",
    }

    def __init__(
        self_,
        connections: Union[List[ListConnectionsResponseDataAttributesConnectionsItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param connections:
        :type connections: [ListConnectionsResponseDataAttributesConnectionsItems], optional
        """
        if connections is not unset:
            kwargs["connections"] = connections
        super().__init__(kwargs)
