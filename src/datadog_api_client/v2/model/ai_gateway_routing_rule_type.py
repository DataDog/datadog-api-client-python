# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRoutingRuleType(ModelSimple):
    """
    AI Gateway routing rule resource type.

    :param value: If omitted defaults to "routing-rules". Must be one of ["routing-rules"].
    :type value: str
    """

    allowed_values = {
        "routing-rules",
    }
    ROUTING_RULES: ClassVar["AiGatewayRoutingRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRoutingRuleType.ROUTING_RULES = AiGatewayRoutingRuleType("routing-rules")
