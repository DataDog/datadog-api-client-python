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
    from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
    from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType


class TeamSyncAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
        from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType

        return {
            "source": (TeamSyncAttributesSource,),
            "type": (TeamSyncAttributesType,),
        }

    attribute_map = {
        "source": "source",
        "type": "type",
    }

    def __init__(self_, source: TeamSyncAttributesSource, type: TeamSyncAttributesType, **kwargs):
        """
        Team sync attributes.

        :param source: The external source platform for team synchronization. Only "github" is supported.
        :type source: TeamSyncAttributesSource

        :param type: The type of synchronization operation. Only "link" is supported, which links existing teams by matching names.
        :type type: TeamSyncAttributesType
        """
        super().__init__(kwargs)

        self_.source = source
        self_.type = type
