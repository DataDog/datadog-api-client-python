# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRoutingRuleTierOrdering(ModelSimple):
    """
    How a tier orders its targets.

    :param value: Must be one of ["configured", "weighted_affinity"].
    :type value: str
    """

    allowed_values = {
        "configured",
        "weighted_affinity",
    }
    CONFIGURED: ClassVar["AiGatewayRoutingRuleTierOrdering"]
    WEIGHTED_AFFINITY: ClassVar["AiGatewayRoutingRuleTierOrdering"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRoutingRuleTierOrdering.CONFIGURED = AiGatewayRoutingRuleTierOrdering("configured")
AiGatewayRoutingRuleTierOrdering.WEIGHTED_AFFINITY = AiGatewayRoutingRuleTierOrdering("weighted_affinity")
