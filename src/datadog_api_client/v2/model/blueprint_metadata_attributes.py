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


class BlueprintMetadataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str,),
            "name": (str,),
            "slug": (str,),
            "tags": ([str],),
            "tile_background": (str,),
            "tile_icon_action_fqn": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "name": "name",
        "slug": "slug",
        "tags": "tags",
        "tile_background": "tile_background",
        "tile_icon_action_fqn": "tile_icon_action_fqn",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        description: str,
        name: str,
        slug: str,
        updated_at: datetime,
        tags: Union[List[str], UnsetType] = unset,
        tile_background: Union[str, UnsetType] = unset,
        tile_icon_action_fqn: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a blueprint metadata resource.

        :param created_at: The timestamp when the blueprint was created.
        :type created_at: datetime

        :param description: A description of what the blueprint does.
        :type description: str

        :param name: The human-readable name of the blueprint.
        :type name: str

        :param slug: The unique slug identifier of the blueprint.
        :type slug: str

        :param tags: Tags associated with the blueprint.
        :type tags: [str], optional

        :param tile_background: The background style of the blueprint tile.
        :type tile_background: str, optional

        :param tile_icon_action_fqn: The fully qualified name of the action used as the tile icon.
        :type tile_icon_action_fqn: str, optional

        :param updated_at: The timestamp when the blueprint was last updated.
        :type updated_at: datetime
        """
        if tags is not unset:
            kwargs["tags"] = tags
        if tile_background is not unset:
            kwargs["tile_background"] = tile_background
        if tile_icon_action_fqn is not unset:
            kwargs["tile_icon_action_fqn"] = tile_icon_action_fqn
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.description = description
        self_.name = name
        self_.slug = slug
        self_.updated_at = updated_at
