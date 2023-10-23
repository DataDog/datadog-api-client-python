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
    from datadog_api_client.v2.model.container_image_group_attributes import ContainerImageGroupAttributes
    from datadog_api_client.v2.model.container_image_group_relationships import ContainerImageGroupRelationships
    from datadog_api_client.v2.model.container_image_group_type import ContainerImageGroupType


class ContainerImageGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_group_attributes import ContainerImageGroupAttributes
        from datadog_api_client.v2.model.container_image_group_relationships import ContainerImageGroupRelationships
        from datadog_api_client.v2.model.container_image_group_type import ContainerImageGroupType

        return {
            "attributes": (ContainerImageGroupAttributes,),
            "id": (str,),
            "relationships": (ContainerImageGroupRelationships,),
            "type": (ContainerImageGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ContainerImageGroupAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ContainerImageGroupRelationships, UnsetType] = unset,
        type: Union[ContainerImageGroupType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Container Image Group object.

        :param attributes: Attributes for a Container Image Group.
        :type attributes: ContainerImageGroupAttributes, optional

        :param id: Container Image Group ID.
        :type id: str, optional

        :param relationships: Relationships inside a Container Image Group.
        :type relationships: ContainerImageGroupRelationships, optional

        :param type: Type of Container Image Group.
        :type type: ContainerImageGroupType, optional
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
