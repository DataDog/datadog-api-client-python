# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRoutingRuleTierOrderingIssue(ModelSimple):
    """
    Stored tier ordering is inconsistent. mixed means targets have different supported orderings, and unknown means a target has an unsupported ordering. The tier is reported as configured without weights. Replace the rule to repair it. Omitted for consistent tiers. A forced deletion cannot rewrite a surviving tier with an unknown issue.

    :param value: Must be one of ["mixed", "unknown"].
    :type value: str
    """

    allowed_values = {
        "mixed",
        "unknown",
    }
    MIXED: ClassVar["AiGatewayRoutingRuleTierOrderingIssue"]
    UNKNOWN: ClassVar["AiGatewayRoutingRuleTierOrderingIssue"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRoutingRuleTierOrderingIssue.MIXED = AiGatewayRoutingRuleTierOrderingIssue("mixed")
AiGatewayRoutingRuleTierOrderingIssue.UNKNOWN = AiGatewayRoutingRuleTierOrderingIssue("unknown")
