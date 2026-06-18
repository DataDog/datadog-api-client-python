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
    from datadog_api_client.v2.model.ticket_creation_rule_attributes_response import (
        TicketCreationRuleAttributesResponse,
    )
    from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType


class TicketCreationRuleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ticket_creation_rule_attributes_response import (
            TicketCreationRuleAttributesResponse,
        )
        from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType

        return {
            "attributes": (TicketCreationRuleAttributesResponse,),
            "id": (UUID,),
            "type": (TicketCreationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TicketCreationRuleAttributesResponse, id: UUID, type: TicketCreationRuleType, **kwargs
    ):
        """
        The data object for a ticket creation rule returned by the API.

        :param attributes: Attributes of a ticket creation rule returned by the API.
        :type attributes: TicketCreationRuleAttributesResponse

        :param id: The ID of the ticket creation rule.
        :type id: UUID

        :param type: The JSON:API type for ticket creation rules.
        :type type: TicketCreationRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
