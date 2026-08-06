# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_detection_update_state import (
        GovernanceControlDetectionUpdateState,
    )


class GovernanceControlDetectionUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_update_state import (
            GovernanceControlDetectionUpdateState,
        )

        return {
            "assigned_team": (str,),
            "assigned_to": (str,),
            "mitigate_after": (datetime,),
            "state": (GovernanceControlDetectionUpdateState,),
        }

    attribute_map = {
        "assigned_team": "assigned_team",
        "assigned_to": "assigned_to",
        "mitigate_after": "mitigate_after",
        "state": "state",
    }

    def __init__(
        self_,
        assigned_team: Union[str, UnsetType] = unset,
        assigned_to: Union[str, UnsetType] = unset,
        mitigate_after: Union[datetime, UnsetType] = unset,
        state: Union[GovernanceControlDetectionUpdateState, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance control detection that can be updated. Only the attributes present in the request are modified.

        :param assigned_team: The handle of the team the detection is assigned to. Set to an empty string to clear the assignment.
        :type assigned_team: str, optional

        :param assigned_to: The UUID of the user the detection is assigned to. Set to an empty string to clear the assignment.
        :type assigned_to: str, optional

        :param mitigate_after: The timestamp after which the detection becomes eligible for mitigation. Used to defer mitigation to a later time.
        :type mitigate_after: datetime, optional

        :param state: The new state to set for the detection. Set to ``exception`` to acknowledge the detection and exclude it from active counts, or ``active`` to reopen it.
        :type state: GovernanceControlDetectionUpdateState, optional
        """
        if assigned_team is not unset:
            kwargs["assigned_team"] = assigned_team
        if assigned_to is not unset:
            kwargs["assigned_to"] = assigned_to
        if mitigate_after is not unset:
            kwargs["mitigate_after"] = mitigate_after
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)
