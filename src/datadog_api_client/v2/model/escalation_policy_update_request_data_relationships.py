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
    from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships_teams import (
        EscalationPolicyUpdateRequestDataRelationshipsTeams,
    )


class EscalationPolicyUpdateRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships_teams import (
            EscalationPolicyUpdateRequestDataRelationshipsTeams,
        )

        return {
            "teams": (EscalationPolicyUpdateRequestDataRelationshipsTeams,),
        }

    attribute_map = {
        "teams": "teams",
    }

    def __init__(self_, teams: Union[EscalationPolicyUpdateRequestDataRelationshipsTeams, UnsetType] = unset, **kwargs):
        """
        Represents relationships in an escalation policy update request, including references to teams.

        :param teams: Defines the relationship to teams within an escalation policy update request, referencing the teams to be associated with or removed from the policy.
        :type teams: EscalationPolicyUpdateRequestDataRelationshipsTeams, optional
        """
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
