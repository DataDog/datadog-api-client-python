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


class SegmentUser(ModelNormal):
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
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Datadog user who created, modified, or disabled a segment.

        :param handle: Handle of the user.
        :type handle: str, optional

        :param icon: URL of the user avatar.
        :type icon: str, optional

        :param id: Numeric ID of the user, as a string.
        :type id: str, optional

        :param name: Name of the user.
        :type name: str, optional

        :param uuid: UUID of the user.
        :type uuid: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)
