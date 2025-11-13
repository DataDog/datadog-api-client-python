# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.connected_team_ref_data import ConnectedTeamRefData


class ConnectedTeamRef(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connected_team_ref_data import ConnectedTeamRefData

        return {
            "data": (ConnectedTeamRefData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ConnectedTeamRefData, UnsetType] = unset, **kwargs):
        """
        Reference to a team from an external system.

        :param data: Reference to connected external team.
        :type data: ConnectedTeamRefData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
