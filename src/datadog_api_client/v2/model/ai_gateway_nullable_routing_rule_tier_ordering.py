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
    How a tier orders its targets. Omission preserves the saved same-position tier on update; null resets to configured. New tiers default to configured. The weighted_affinity ordering distributes first-choice assignments by relative target weights and accepts only model targets with an explicit provider, without repeated provider and model pairs in the same tier. The `classified` ordering is allowed only in the first tier and requires a classifier, destination rubrics, and one default destination.

    :param value: Must be one of ["configured", "weighted_affinity", "classified"].
    :type value: str
    """

    allowed_values = {
        "configured",
        "weighted_affinity",
        "classified",
    }
    CONFIGURED: ClassVar["AiGatewayNullableRoutingRuleTierOrdering"]
    WEIGHTED_AFFINITY: ClassVar["AiGatewayNullableRoutingRuleTierOrdering"]
    CLASSIFIED: ClassVar["AiGatewayNullableRoutingRuleTierOrdering"]

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
AiGatewayNullableRoutingRuleTierOrdering.CLASSIFIED = AiGatewayNullableRoutingRuleTierOrdering("classified")
