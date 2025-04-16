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
    from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams_data_items_type import (
        EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType,
    )


class EscalationPolicyCreateRequestDataRelationshipsTeamsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams_data_items_type import (
            EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType, **kwargs):
        """
        Defines a single relationship to a team within an escalation policy creation request. Contains the team's ``id`` and ``type``.

        :param id: Specifies the unique identifier for the related team.
        :type id: str

        :param type: Indicates that the resource is of type ``teams``.
        :type type: EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
