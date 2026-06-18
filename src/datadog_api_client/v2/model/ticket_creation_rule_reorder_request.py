# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ticket_creation_rule_reorder_item import TicketCreationRuleReorderItem


class TicketCreationRuleReorderRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ticket_creation_rule_reorder_item import TicketCreationRuleReorderItem

        return {
            "data": ([TicketCreationRuleReorderItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[TicketCreationRuleReorderItem], **kwargs):
        """
        The body of the ticket creation rule reorder request.

        :param data: The ordered list of all ticket creation rules; every rule must be included.
        :type data: [TicketCreationRuleReorderItem]
        """
        super().__init__(kwargs)

        self_.data = data
