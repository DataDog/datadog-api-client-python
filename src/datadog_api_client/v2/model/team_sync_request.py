# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_sync_data import TeamSyncData


class TeamSyncRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_data import TeamSyncData

        return {
            "data": (TeamSyncData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TeamSyncData, **kwargs):
        """
        Team sync request.

        :param data: Team sync data.
        :type data: TeamSyncData
        """
        super().__init__(kwargs)

        self_.data = data
