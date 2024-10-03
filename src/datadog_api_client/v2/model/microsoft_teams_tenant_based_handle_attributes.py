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


class MicrosoftTeamsTenantBasedHandleAttributes(ModelNormal):
    validations = {
        "channel_id": {
            "max_length": 255,
        },
        "name": {
            "max_length": 255,
        },
        "team_id": {
            "max_length": 255,
        },
        "tenant_id": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "channel_id": (str,),
            "name": (str,),
            "team_id": (str,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "channel_id": "channel_id",
        "name": "name",
        "team_id": "team_id",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        channel_id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Tenant-based handle attributes.

        :param channel_id: Channel id.
        :type channel_id: str, optional

        :param name: Tenant-based handle name.
        :type name: str, optional

        :param team_id: Team id.
        :type team_id: str, optional

        :param tenant_id: Tenant id.
        :type tenant_id: str, optional
        """
        if channel_id is not unset:
            kwargs["channel_id"] = channel_id
        if name is not unset:
            kwargs["name"] = name
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        super().__init__(kwargs)
