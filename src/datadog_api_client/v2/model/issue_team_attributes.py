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


class IssueTeamAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "name": (str,),
            "summary": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "name": "name",
        "summary": "summary",
    }

    def __init__(
        self_,
        handle: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a team.

        :param handle: The team's identifier.
        :type handle: str, optional

        :param name: The name of the team.
        :type name: str, optional

        :param summary: A brief summary of the team, derived from its description.
        :type summary: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if name is not unset:
            kwargs["name"] = name
        if summary is not unset:
            kwargs["summary"] = summary
        super().__init__(kwargs)
