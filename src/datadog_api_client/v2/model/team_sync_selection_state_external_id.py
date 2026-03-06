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
    from datadog_api_client.v2.model.team_sync_selection_state_external_id_type import (
        TeamSyncSelectionStateExternalIdType,
    )


class TeamSyncSelectionStateExternalId(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_selection_state_external_id_type import (
            TeamSyncSelectionStateExternalIdType,
        )

        return {
            "type": (TeamSyncSelectionStateExternalIdType,),
            "value": (str,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: TeamSyncSelectionStateExternalIdType, value: str, **kwargs):
        """
        The external identifier for a team or organization in the source platform.

        :param type: The type of external identifier for the selection state item.
            For GitHub synchronization, the allowed values are ``team`` and
            ``organization``.
        :type type: TeamSyncSelectionStateExternalIdType

        :param value: The external identifier value from the source
            platform. For GitHub, this is the string
            representation of a GitHub organization ID or team
            ID.
        :type value: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
