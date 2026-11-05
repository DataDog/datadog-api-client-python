# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelPricingEffectiveSource(ModelSimple):
    """
    Effective source of the model pricing data.

    :param value: Must be one of ["catalog_auto", "model_override", "unknown"].
    :type value: str
    """

    allowed_values = {
        "catalog_auto",
        "model_override",
        "unknown",
    }
    CATALOG_AUTO: ClassVar["AiGatewayModelPricingEffectiveSource"]
    MODEL_OVERRIDE: ClassVar["AiGatewayModelPricingEffectiveSource"]
    UNKNOWN: ClassVar["AiGatewayModelPricingEffectiveSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelPricingEffectiveSource.CATALOG_AUTO = AiGatewayModelPricingEffectiveSource("catalog_auto")
AiGatewayModelPricingEffectiveSource.MODEL_OVERRIDE = AiGatewayModelPricingEffectiveSource("model_override")
AiGatewayModelPricingEffectiveSource.UNKNOWN = AiGatewayModelPricingEffectiveSource("unknown")
