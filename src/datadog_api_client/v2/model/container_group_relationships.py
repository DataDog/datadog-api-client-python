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
    from datadog_api_client.v2.model.container_group_relationships_link import ContainerGroupRelationshipsLink


class ContainerGroupRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_group_relationships_link import ContainerGroupRelationshipsLink

        return {
            "containers": (ContainerGroupRelationshipsLink,),
        }

    attribute_map = {
        "containers": "containers",
    }

    def __init__(self_, containers: Union[ContainerGroupRelationshipsLink, UnsetType] = unset, **kwargs):
        """
        Relationships to containers inside a container group.

        :param containers: Relationships to Containers inside a Container Group.
        :type containers: ContainerGroupRelationshipsLink, optional
        """
        if containers is not unset:
            kwargs["containers"] = containers
        super().__init__(kwargs)
