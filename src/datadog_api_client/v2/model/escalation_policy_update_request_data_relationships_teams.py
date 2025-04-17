# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships_teams_data_items import (
        EscalationPolicyUpdateRequestDataRelationshipsTeamsDataItems,
    )


class EscalationPolicyUpdateRequestDataRelationshipsTeams(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships_teams_data_items import (
            EscalationPolicyUpdateRequestDataRelationshipsTeamsDataItems,
        )

        return {
            "data": ([EscalationPolicyUpdateRequestDataRelationshipsTeamsDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: Union[List[EscalationPolicyUpdateRequestDataRelationshipsTeamsDataItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the relationship to teams within an escalation policy update request, referencing the teams to be associated with or removed from the policy.

        :param data: An array of team references for the escalation policy update.
        :type data: [EscalationPolicyUpdateRequestDataRelationshipsTeamsDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
