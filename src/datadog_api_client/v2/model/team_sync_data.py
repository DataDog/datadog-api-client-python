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
    from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
    from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType


class TeamSyncData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
        from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType

        return {
            "attributes": (TeamSyncAttributes,),
            "type": (TeamSyncBulkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TeamSyncAttributes, type: TeamSyncBulkType, **kwargs):
        """
        Team sync data.

        :param attributes: Team sync attributes.
        :type attributes: TeamSyncAttributes

        :param type: Team sync bulk type.
        :type type: TeamSyncBulkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
