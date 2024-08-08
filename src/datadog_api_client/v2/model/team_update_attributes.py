# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class TeamUpdateAttributes(ModelNormal):
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
    }

    @cached_property
    def openapi_types(_):
        return {
            "avatar": (str, none_type),
            "banner": (int, none_type),
            "description": (str,),
            "handle": (str,),
            "handles": (str,),
            "hidden_modules": ([str],),
            "link_count": (int,),
            "name": (str,),
            "summary": (str,),
            "visible_modules": ([str],),
        }

    attribute_map = {
        "avatar": "avatar",
        "banner": "banner",
        "description": "description",
        "handle": "handle",
        "handles": "handles",
        "hidden_modules": "hidden_modules",
        "link_count": "link_count",
        "name": "name",
        "summary": "summary",
        "visible_modules": "visible_modules",
    }
    read_only_vars = {
        "link_count",
        "summary",
    }

    def __init__(
        self_,
        handle: str,
        name: str,
        avatar: Union[str, none_type, UnsetType] = unset,
        banner: Union[int, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        handles: Union[str, UnsetType] = unset,
        hidden_modules: Union[List[str], UnsetType] = unset,
        link_count: Union[int, UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        visible_modules: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Team update attributes

        :param avatar: Unicode representation of the avatar for the team, limited to a single grapheme
        :type avatar: str, none_type, optional

        :param banner: Banner selection for the team
        :type banner: int, none_type, optional

        :param description: Free-form markdown description/content for the team's homepage
        :type description: str, optional

        :param handle: The team's identifier
        :type handle: str

        :param handles: The TeamUpdateAttributes handles.
        :type handles: str, optional

        :param hidden_modules: Collection of hidden modules for the team
        :type hidden_modules: [str], optional

        :param link_count: The number of links belonging to the team
        :type link_count: int, optional

        :param name: The name of the team
        :type name: str

        :param summary: A brief summary of the team
        :type summary: str, optional

        :param visible_modules: Collection of visible modules for the team
        :type visible_modules: [str], optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if banner is not unset:
            kwargs["banner"] = banner
        if description is not unset:
            kwargs["description"] = description
        if handles is not unset:
            kwargs["handles"] = handles
        if hidden_modules is not unset:
            kwargs["hidden_modules"] = hidden_modules
        if link_count is not unset:
            kwargs["link_count"] = link_count
        if summary is not unset:
            kwargs["summary"] = summary
        if visible_modules is not unset:
            kwargs["visible_modules"] = visible_modules
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
