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


class IncidentMSTeamsChannel(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ms_channel_id": (str,),
            "ms_channel_name": (str,),
            "ms_team_id": (str,),
            "ms_tenant_id": (str,),
            "redirect_url": (str,),
            "team_name": (str,),
        }

    attribute_map = {
        "ms_channel_id": "ms_channel_id",
        "ms_channel_name": "ms_channel_name",
        "ms_team_id": "ms_team_id",
        "ms_tenant_id": "ms_tenant_id",
        "redirect_url": "redirect_url",
        "team_name": "team_name",
    }

    def __init__(
        self_,
        ms_channel_id: str,
        ms_channel_name: str,
        ms_team_id: Union[str, UnsetType] = unset,
        ms_tenant_id: Union[str, UnsetType] = unset,
        redirect_url: Union[str, UnsetType] = unset,
        team_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Microsoft Teams channel associated with an incident.

        :param ms_channel_id: The Teams channel identifier.
        :type ms_channel_id: str

        :param ms_channel_name: The name of the Teams channel.
        :type ms_channel_name: str

        :param ms_team_id: The Teams team identifier.
        :type ms_team_id: str, optional

        :param ms_tenant_id: The Teams tenant identifier.
        :type ms_tenant_id: str, optional

        :param redirect_url: The redirect URL for the channel.
        :type redirect_url: str, optional

        :param team_name: The name of the Teams team.
        :type team_name: str, optional
        """
        if ms_team_id is not unset:
            kwargs["ms_team_id"] = ms_team_id
        if ms_tenant_id is not unset:
            kwargs["ms_tenant_id"] = ms_tenant_id
        if redirect_url is not unset:
            kwargs["redirect_url"] = redirect_url
        if team_name is not unset:
            kwargs["team_name"] = team_name
        super().__init__(kwargs)

        self_.ms_channel_id = ms_channel_id
        self_.ms_channel_name = ms_channel_name
