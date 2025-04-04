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


class TeamReferenceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avatar": (str,),
            "description": (str,),
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "avatar": "avatar",
        "description": "description",
        "handle": "handle",
        "name": "name",
    }

    def __init__(
        self_,
        avatar: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.

        :param avatar: URL or reference for the team's avatar (if available).
        :type avatar: str, optional

        :param description: A short text describing the team.
        :type description: str, optional

        :param handle: A unique handle/slug for the team.
        :type handle: str, optional

        :param name: The full, human-readable name of the team.
        :type name: str, optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if description is not unset:
            kwargs["description"] = description
        if handle is not unset:
            kwargs["handle"] = handle
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
