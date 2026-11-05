# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayNullableRoutingRuleTierOrdering(ModelSimple):
    """
    How a tier orders its targets. Omitted or null defaults to configured, which preserves target order. The weighted_affinity ordering distributes first-choice assignments by relative target weights and accepts only model targets with an explicit provider, without repeated provider and model pairs in the same tier.

    :param value: If omitted defaults to "configured". Must be one of ["configured", "weighted_affinity"].
    :type value: str
    """

    allowed_values = {
        "configured",
        "weighted_affinity",
    }
    CONFIGURED: ClassVar["AiGatewayNullableRoutingRuleTierOrdering"]
    WEIGHTED_AFFINITY: ClassVar["AiGatewayNullableRoutingRuleTierOrdering"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayNullableRoutingRuleTierOrdering.CONFIGURED = AiGatewayNullableRoutingRuleTierOrdering("configured")
AiGatewayNullableRoutingRuleTierOrdering.WEIGHTED_AFFINITY = AiGatewayNullableRoutingRuleTierOrdering(
    "weighted_affinity"
)
