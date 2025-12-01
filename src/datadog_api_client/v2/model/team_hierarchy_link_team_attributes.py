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


class TeamHierarchyLinkTeamAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avatar": (str, none_type),
            "banner": (int,),
            "handle": (str,),
            "is_managed": (bool,),
            "is_open_membership": (bool,),
            "link_count": (int,),
            "name": (str,),
            "summary": (str, none_type),
            "user_count": (int,),
        }

    attribute_map = {
        "avatar": "avatar",
        "banner": "banner",
        "handle": "handle",
        "is_managed": "is_managed",
        "is_open_membership": "is_open_membership",
        "link_count": "link_count",
        "name": "name",
        "summary": "summary",
        "user_count": "user_count",
    }

    def __init__(
        self_,
        handle: str,
        name: str,
        avatar: Union[str, none_type, UnsetType] = unset,
        banner: Union[int, UnsetType] = unset,
        is_managed: Union[bool, UnsetType] = unset,
        is_open_membership: Union[bool, UnsetType] = unset,
        link_count: Union[int, UnsetType] = unset,
        summary: Union[str, none_type, UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.

        :param avatar: The team's avatar
        :type avatar: str, none_type, optional

        :param banner: The team's banner
        :type banner: int, optional

        :param handle: The team's handle
        :type handle: str

        :param is_managed: Whether the team is managed
        :type is_managed: bool, optional

        :param is_open_membership: Whether the team has open membership
        :type is_open_membership: bool, optional

        :param link_count: The number of links for the team
        :type link_count: int, optional

        :param name: The team's name
        :type name: str

        :param summary: The team's summary
        :type summary: str, none_type, optional

        :param user_count: The number of users in the team
        :type user_count: int, optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if banner is not unset:
            kwargs["banner"] = banner
        if is_managed is not unset:
            kwargs["is_managed"] = is_managed
        if is_open_membership is not unset:
            kwargs["is_open_membership"] = is_open_membership
        if link_count is not unset:
            kwargs["link_count"] = link_count
        if summary is not unset:
            kwargs["summary"] = summary
        if user_count is not unset:
            kwargs["user_count"] = user_count
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
