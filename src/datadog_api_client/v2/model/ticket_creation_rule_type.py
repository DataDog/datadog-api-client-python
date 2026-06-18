# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TicketCreationRuleType(ModelSimple):
    """
    The JSON:API type for ticket creation rules.

    :param value: If omitted defaults to "ticket_creation_rules". Must be one of ["ticket_creation_rules"].
    :type value: str
    """

    allowed_values = {
        "ticket_creation_rules",
    }
    TICKET_CREATION_RULES: ClassVar["TicketCreationRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TicketCreationRuleType.TICKET_CREATION_RULES = TicketCreationRuleType("ticket_creation_rules")
