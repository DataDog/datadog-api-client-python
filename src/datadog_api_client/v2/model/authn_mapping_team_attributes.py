# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class AuthNMappingTeamAttributes(ModelNormal):
    validations = {
        "handle": {
            "max_length": 195,
        },
        "link_count": {
            "inclusive_maximum": 2147483647,
        },
        "name": {
            "max_length": 200,
        },
        "summary": {
            "max_length": 120,
        },
        "user_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avatar": (str, none_type),
            "banner": (int, none_type),
            "handle": (str,),
            "link_count": (int,),
            "name": (str,),
            "summary": (str, none_type),
            "user_count": (int,),
        }

    attribute_map = {
        "avatar": "avatar",
        "banner": "banner",
        "handle": "handle",
        "link_count": "link_count",
        "name": "name",
        "summary": "summary",
        "user_count": "user_count",
    }
    read_only_vars = {
        "link_count",
        "user_count",
    }

    def __init__(
        self_,
        avatar: Union[str, none_type, UnsetType] = unset,
        banner: Union[int, none_type, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        link_count: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        summary: Union[str, none_type, UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team attributes.

        :param avatar: Unicode representation of the avatar for the team, limited to a single grapheme
        :type avatar: str, none_type, optional

        :param banner: Banner selection for the team
        :type banner: int, none_type, optional

        :param handle: The team's identifier
        :type handle: str, optional

        :param link_count: The number of links belonging to the team
        :type link_count: int, optional

        :param name: The name of the team
        :type name: str, optional

        :param summary: A brief summary of the team, derived from the ``description``
        :type summary: str, none_type, optional

        :param user_count: The number of users belonging to the team
        :type user_count: int, optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if banner is not unset:
            kwargs["banner"] = banner
        if handle is not unset:
            kwargs["handle"] = handle
        if link_count is not unset:
            kwargs["link_count"] = link_count
        if name is not unset:
            kwargs["name"] = name
        if summary is not unset:
            kwargs["summary"] = summary
        if user_count is not unset:
            kwargs["user_count"] = user_count
        super().__init__(kwargs)
