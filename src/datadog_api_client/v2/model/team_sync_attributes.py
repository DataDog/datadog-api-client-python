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
    from datadog_api_client.v2.model.team_sync_attributes_frequency import TeamSyncAttributesFrequency
    from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
    from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType


class TeamSyncAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_attributes_frequency import TeamSyncAttributesFrequency
        from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
        from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType

        return {
            "frequency": (TeamSyncAttributesFrequency,),
            "source": (TeamSyncAttributesSource,),
            "sync_membership": (bool,),
            "type": (TeamSyncAttributesType,),
        }

    attribute_map = {
        "frequency": "frequency",
        "source": "source",
        "sync_membership": "sync_membership",
        "type": "type",
    }

    def __init__(
        self_,
        source: TeamSyncAttributesSource,
        type: TeamSyncAttributesType,
        frequency: Union[TeamSyncAttributesFrequency, UnsetType] = unset,
        sync_membership: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team sync attributes.

        :param frequency: How often the sync process should be run. Defaults to ``once`` when not provided.
        :type frequency: TeamSyncAttributesFrequency, optional

        :param source: The external source platform for team synchronization. Only "github" is supported.
        :type source: TeamSyncAttributesSource

        :param sync_membership: Whether to sync members from the external team to the Datadog team. Defaults to ``false`` when not provided.
        :type sync_membership: bool, optional

        :param type: The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found.
        :type type: TeamSyncAttributesType
        """
        if frequency is not unset:
            kwargs["frequency"] = frequency
        if sync_membership is not unset:
            kwargs["sync_membership"] = sync_membership
        super().__init__(kwargs)

        self_.source = source
        self_.type = type
