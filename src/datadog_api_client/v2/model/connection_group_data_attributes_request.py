# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ConnectionGroupDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connections": ([str],),
            "description": (str,),
            "integration_type": (str,),
            "name": (str,),
            "policy_attributes": (str,),
            "tag_keys": ([str],),
        }

    attribute_map = {
        "connections": "connections",
        "description": "description",
        "integration_type": "integration_type",
        "name": "name",
        "policy_attributes": "policy_attributes",
        "tag_keys": "tag_keys",
    }

    def __init__(
        self_,
        connections: Union[List[str], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        integration_type: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        policy_attributes: Union[str, UnsetType] = unset,
        tag_keys: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a connection group.

        :param connections: List of connection IDs associated with the connection group.
        :type connections: [str], optional

        :param description: The description of the connection group.
        :type description: str, optional

        :param integration_type: The integration type of the connection group.
        :type integration_type: str, optional

        :param name: The name of the connection group.
        :type name: str, optional

        :param policy_attributes: Policy attributes for the connection group.
        :type policy_attributes: str, optional

        :param tag_keys: Tag keys associated with the connection group.
        :type tag_keys: [str], optional
        """
        if connections is not unset:
            kwargs["connections"] = connections
        if description is not unset:
            kwargs["description"] = description
        if integration_type is not unset:
            kwargs["integration_type"] = integration_type
        if name is not unset:
            kwargs["name"] = name
        if policy_attributes is not unset:
            kwargs["policy_attributes"] = policy_attributes
        if tag_keys is not unset:
            kwargs["tag_keys"] = tag_keys
        super().__init__(kwargs)
