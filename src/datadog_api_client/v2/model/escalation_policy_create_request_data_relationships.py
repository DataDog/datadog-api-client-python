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
    from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams import (
        EscalationPolicyCreateRequestDataRelationshipsTeams,
    )


class EscalationPolicyCreateRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams import (
            EscalationPolicyCreateRequestDataRelationshipsTeams,
        )

        return {
            "teams": (EscalationPolicyCreateRequestDataRelationshipsTeams,),
        }

    attribute_map = {
        "teams": "teams",
    }

    def __init__(self_, teams: Union[EscalationPolicyCreateRequestDataRelationshipsTeams, UnsetType] = unset, **kwargs):
        """
        Represents relationships in an escalation policy creation request, including references to teams.

        :param teams: Defines the relationship to teams within an escalation policy creation request, referencing the teams to be associated with the policy.
        :type teams: EscalationPolicyCreateRequestDataRelationshipsTeams, optional
        """
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
