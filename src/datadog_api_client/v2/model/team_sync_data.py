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
    from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
    from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType


class TeamSyncData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
        from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType

        return {
            "attributes": (TeamSyncAttributes,),
            "id": (str,),
            "type": (TeamSyncBulkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TeamSyncAttributes, type: TeamSyncBulkType, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        A configuration governing syncing between Datadog teams and teams from an external system.

        :param attributes: Team sync attributes.
        :type attributes: TeamSyncAttributes

        :param id: The sync's identifier
        :type id: str, optional

        :param type: Team sync bulk type.
        :type type: TeamSyncBulkType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
