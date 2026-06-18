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
    from datadog_api_client.v2.model.ticket_creation_rule_data_response import TicketCreationRuleDataResponse
    from datadog_api_client.v2.model.security_automation_rules_links import SecurityAutomationRulesLinks
    from datadog_api_client.v2.model.security_automation_rules_meta import SecurityAutomationRulesMeta


class TicketCreationRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ticket_creation_rule_data_response import TicketCreationRuleDataResponse
        from datadog_api_client.v2.model.security_automation_rules_links import SecurityAutomationRulesLinks
        from datadog_api_client.v2.model.security_automation_rules_meta import SecurityAutomationRulesMeta

        return {
            "data": ([TicketCreationRuleDataResponse],),
            "links": (SecurityAutomationRulesLinks,),
            "meta": (SecurityAutomationRulesMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[TicketCreationRuleDataResponse],
        links: SecurityAutomationRulesLinks,
        meta: SecurityAutomationRulesMeta,
        **kwargs,
    ):
        """
        A list of ticket creation rules with pagination metadata.

        :param data: A list of ticket creation rule data objects.
        :type data: [TicketCreationRuleDataResponse]

        :param links: Pagination links for the list of automation rules.
        :type links: SecurityAutomationRulesLinks

        :param meta: Metadata for the list of automation rules.
        :type meta: SecurityAutomationRulesMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
        self_.meta = meta
