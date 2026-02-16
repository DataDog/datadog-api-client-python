# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ConnectionGroupDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connections": ([str],),
            "created_at": (datetime,),
            "description": (str,),
            "integration_type": (str,),
            "is_favorite": (bool,),
            "last_updated_at": (datetime,),
            "name": (str,),
            "tag_keys": ([str],),
        }

    attribute_map = {
        "connections": "connections",
        "created_at": "created_at",
        "description": "description",
        "integration_type": "integration_type",
        "is_favorite": "is_favorite",
        "last_updated_at": "last_updated_at",
        "name": "name",
        "tag_keys": "tag_keys",
    }

    def __init__(
        self_,
        created_at: datetime,
        integration_type: str,
        is_favorite: bool,
        last_updated_at: datetime,
        name: str,
        tag_keys: List[str],
        connections: Union[List[str], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a connection group.

        :param connections: List of connection IDs associated with the connection group.
        :type connections: [str], optional

        :param created_at: The creation timestamp of the connection group.
        :type created_at: datetime

        :param description: The description of the connection group.
        :type description: str, optional

        :param integration_type: The integration type of the connection group.
        :type integration_type: str

        :param is_favorite: Indicates if the connection group is marked as favorite.
        :type is_favorite: bool

        :param last_updated_at: The last updated timestamp of the connection group.
        :type last_updated_at: datetime

        :param name: The name of the connection group.
        :type name: str

        :param tag_keys: Tag keys associated with the connection group.
        :type tag_keys: [str]
        """
        if connections is not unset:
            kwargs["connections"] = connections
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.integration_type = integration_type
        self_.is_favorite = is_favorite
        self_.last_updated_at = last_updated_at
        self_.name = name
        self_.tag_keys = tag_keys
