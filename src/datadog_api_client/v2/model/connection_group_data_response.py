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
    from datadog_api_client.v2.model.connection_group_data_attributes_response import (
        ConnectionGroupDataAttributesResponse,
    )
    from datadog_api_client.v2.model.connection_group_relationships import ConnectionGroupRelationships
    from datadog_api_client.v2.model.connection_group_type import ConnectionGroupType


class ConnectionGroupDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connection_group_data_attributes_response import (
            ConnectionGroupDataAttributesResponse,
        )
        from datadog_api_client.v2.model.connection_group_relationships import ConnectionGroupRelationships
        from datadog_api_client.v2.model.connection_group_type import ConnectionGroupType

        return {
            "attributes": (ConnectionGroupDataAttributesResponse,),
            "id": (str,),
            "relationships": (ConnectionGroupRelationships,),
            "type": (ConnectionGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ConnectionGroupDataAttributesResponse,
        id: str,
        type: ConnectionGroupType,
        relationships: Union[ConnectionGroupRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a connection group.

        :param attributes: Attributes of a connection group.
        :type attributes: ConnectionGroupDataAttributesResponse

        :param id: The unique identifier of the connection group.
        :type id: str

        :param relationships: Relationships for a connection group.
        :type relationships: ConnectionGroupRelationships, optional

        :param type: The definition of ``ConnectionGroupType`` object.
        :type type: ConnectionGroupType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
