# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class TeamAttributes(ModelNormal):
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
            "created_at": (datetime,),
            "description": (str, none_type),
            "handle": (str,),
            "hidden_modules": ([str],),
            "link_count": (int,),
            "modified_at": (datetime,),
            "name": (str,),
            "summary": (str, none_type),
            "user_count": (int,),
            "visible_modules": ([str],),
        }

    attribute_map = {
        "avatar": "avatar",
        "banner": "banner",
        "created_at": "created_at",
        "description": "description",
        "handle": "handle",
        "hidden_modules": "hidden_modules",
        "link_count": "link_count",
        "modified_at": "modified_at",
        "name": "name",
        "summary": "summary",
        "user_count": "user_count",
        "visible_modules": "visible_modules",
    }
    read_only_vars = {
        "link_count",
        "user_count",
    }

    def __init__(
        self_,
        handle: str,
        name: str,
        avatar: Union[str, none_type, UnsetType] = unset,
        banner: Union[int, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        hidden_modules: Union[List[str], UnsetType] = unset,
        link_count: Union[int, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        summary: Union[str, none_type, UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        visible_modules: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Team attributes

        :param avatar: Unicode representation of the avatar for the team, limited to a single grapheme
        :type avatar: str, none_type, optional

        :param banner: Banner selection for the team
        :type banner: int, none_type, optional

        :param created_at: Creation date of the team
        :type created_at: datetime, optional

        :param description: Free-form markdown description/content for the team's homepage
        :type description: str, none_type, optional

        :param handle: The team's identifier
        :type handle: str

        :param hidden_modules: Collection of hidden modules for the team
        :type hidden_modules: [str], optional

        :param link_count: The number of links belonging to the team
        :type link_count: int, optional

        :param modified_at: Modification date of the team
        :type modified_at: datetime, optional

        :param name: The name of the team
        :type name: str

        :param summary: A brief summary of the team, derived from the ``description``
        :type summary: str, none_type, optional

        :param user_count: The number of users belonging to the team
        :type user_count: int, optional

        :param visible_modules: Collection of visible modules for the team
        :type visible_modules: [str], optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if banner is not unset:
            kwargs["banner"] = banner
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if hidden_modules is not unset:
            kwargs["hidden_modules"] = hidden_modules
        if link_count is not unset:
            kwargs["link_count"] = link_count
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if summary is not unset:
            kwargs["summary"] = summary
        if user_count is not unset:
            kwargs["user_count"] = user_count
        if visible_modules is not unset:
            kwargs["visible_modules"] = visible_modules
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
