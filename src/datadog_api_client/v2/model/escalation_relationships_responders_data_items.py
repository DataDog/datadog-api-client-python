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
    from datadog_api_client.v2.model.escalation_relationships_responders_data_items_type import (
        EscalationRelationshipsRespondersDataItemsType,
    )


class EscalationRelationshipsRespondersDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_relationships_responders_data_items_type import (
            EscalationRelationshipsRespondersDataItemsType,
        )

        return {
            "id": (str,),
            "type": (EscalationRelationshipsRespondersDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: EscalationRelationshipsRespondersDataItemsType, **kwargs):
        """
        Represents a user assigned to an escalation step.

        :param id: Unique identifier of the user assigned to the escalation step.
        :type id: str

        :param type: Represents the resource type for users assigned as responders in an escalation step.
        :type type: EscalationRelationshipsRespondersDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
