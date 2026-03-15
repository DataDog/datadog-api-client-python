# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class PlaylistDataAttributesCreatedBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "icon": (str,),
            "id": (str,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "icon": "icon",
        "id": "id",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        handle: str,
        id: str,
        uuid: str,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about the user who created the playlist.

        :param handle: Email handle of the user who created the playlist.
        :type handle: str

        :param icon: URL or identifier of the user's avatar icon.
        :type icon: str, optional

        :param id: Unique identifier of the user who created the playlist.
        :type id: str

        :param name: Display name of the user who created the playlist.
        :type name: str, optional

        :param uuid: UUID of the user who created the playlist.
        :type uuid: str
        """
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.handle = handle
        self_.id = id
        self_.uuid = uuid
