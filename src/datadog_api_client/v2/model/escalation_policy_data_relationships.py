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
    from datadog_api_client.v2.model.escalation_policy_data_relationships_steps import (
        EscalationPolicyDataRelationshipsSteps,
    )
    from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams


class EscalationPolicyDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_data_relationships_steps import (
            EscalationPolicyDataRelationshipsSteps,
        )
        from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams

        return {
            "steps": (EscalationPolicyDataRelationshipsSteps,),
            "teams": (DataRelationshipsTeams,),
        }

    attribute_map = {
        "steps": "steps",
        "teams": "teams",
    }

    def __init__(
        self_,
        steps: EscalationPolicyDataRelationshipsSteps,
        teams: Union[DataRelationshipsTeams, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the relationships for an escalation policy, including references to steps and teams.

        :param steps: Defines the relationship to a collection of steps within an escalation policy. Contains an array of step data references.
        :type steps: EscalationPolicyDataRelationshipsSteps

        :param teams: Associates teams with this schedule in a data structure.
        :type teams: DataRelationshipsTeams, optional
        """
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)

        self_.steps = steps
