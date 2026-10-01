# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ticket_creation_rule_attributes_create import TicketCreationRuleAttributesCreate
    from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType


class TicketCreationRuleDataUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ticket_creation_rule_attributes_create import (
            TicketCreationRuleAttributesCreate,
        )
        from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType

        return {
            "attributes": (TicketCreationRuleAttributesCreate,),
            "id": (UUID,),
            "type": (TicketCreationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TicketCreationRuleAttributesCreate, id: UUID, type: TicketCreationRuleType, **kwargs
    ):
        """
        The data object for a ticket creation rule update request. The ``id`` must match the ``rule_id`` path parameter.

        :param attributes: Attributes for creating or updating a ticket creation rule.
        :type attributes: TicketCreationRuleAttributesCreate

        :param id: The ID of the ticket creation rule to update.
        :type id: UUID

        :param type: The JSON:API type for ticket creation rules.
        :type type: TicketCreationRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
