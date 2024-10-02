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


class MicrosoftTeamsChannelInfoResponseAttributes(ModelNormal):
    validations = {
        "is_primary": {
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
            "is_primary": (bool,),
            "team_id": (str,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "is_primary": "is_primary",
        "team_id": "team_id",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        is_primary: Union[bool, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Channel attributes.

        :param is_primary: Indicates if this is the primary channel.
        :type is_primary: bool, optional

        :param team_id: Team id.
        :type team_id: str, optional

        :param tenant_id: Tenant id.
        :type tenant_id: str, optional
        """
        if is_primary is not unset:
            kwargs["is_primary"] = is_primary
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        super().__init__(kwargs)
