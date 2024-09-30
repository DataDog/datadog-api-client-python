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


class AbbreviatedTeamAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avatar": (str, none_type),
            "banner": (int,),
            "handle": (str,),
            "handles": (str,),
            "is_open_membership": (bool,),
            "name": (str,),
            "summary": (str,),
        }

    attribute_map = {
        "avatar": "avatar",
        "banner": "banner",
        "handle": "handle",
        "handles": "handles",
        "is_open_membership": "is_open_membership",
        "name": "name",
        "summary": "summary",
    }
    read_only_vars = {
        "is_open_membership",
        "summary",
    }

    def __init__(
        self_,
        handle: str,
        name: str,
        avatar: Union[str, none_type, UnsetType] = unset,
        banner: Union[int, UnsetType] = unset,
        handles: Union[str, UnsetType] = unset,
        is_open_membership: Union[bool, UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AbbreviatedTeamAttributes`` object.

        :param avatar: Unicode representation of the avatar for the team, limited to a single grapheme
        :type avatar: str, none_type, optional

        :param banner: Banner selection for the team
        :type banner: int, optional

        :param handle: The team's identifier
        :type handle: str

        :param handles: The ``AbbreviatedTeamAttributes`` ``handles``.
        :type handles: str, optional

        :param is_open_membership: The ``AbbreviatedTeamAttributes`` ``is_open_membership``.
        :type is_open_membership: bool, optional

        :param name: The name of the team
        :type name: str

        :param summary: A brief summary of the team
        :type summary: str, optional
        """
        if avatar is not unset:
            kwargs["avatar"] = avatar
        if banner is not unset:
            kwargs["banner"] = banner
        if handles is not unset:
            kwargs["handles"] = handles
        if is_open_membership is not unset:
            kwargs["is_open_membership"] = is_open_membership
        if summary is not unset:
            kwargs["summary"] = summary
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
