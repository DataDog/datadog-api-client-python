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


class TeamHierarchyMemberTeamAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "name": "name",
    }

    def __init__(self_, handle: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Available attributes of the requested team.

        :param handle: Handle of the team.
        :type handle: str, optional

        :param name: Name of the team.
        :type name: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
