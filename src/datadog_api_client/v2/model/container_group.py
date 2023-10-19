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
    from datadog_api_client.v2.model.container_group_attributes import ContainerGroupAttributes
    from datadog_api_client.v2.model.container_group_relationships import ContainerGroupRelationships
    from datadog_api_client.v2.model.container_group_type import ContainerGroupType


class ContainerGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_group_attributes import ContainerGroupAttributes
        from datadog_api_client.v2.model.container_group_relationships import ContainerGroupRelationships
        from datadog_api_client.v2.model.container_group_type import ContainerGroupType

        return {
            "attributes": (ContainerGroupAttributes,),
            "id": (str,),
            "relationships": (ContainerGroupRelationships,),
            "type": (ContainerGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ContainerGroupAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ContainerGroupRelationships, UnsetType] = unset,
        type: Union[ContainerGroupType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Container group object.

        :param attributes: Attributes for a container group.
        :type attributes: ContainerGroupAttributes, optional

        :param id: Container Group ID.
        :type id: str, optional

        :param relationships: Relationships to containers inside a container group.
        :type relationships: ContainerGroupRelationships, optional

        :param type: Type of container group.
        :type type: ContainerGroupType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
