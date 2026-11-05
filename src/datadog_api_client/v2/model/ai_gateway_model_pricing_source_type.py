# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelPricingSourceType(ModelSimple):
    """
    Source type for the pricing configuration.

    :param value: Must be one of ["catalog", "custom"].
    :type value: str
    """

    allowed_values = {
        "catalog",
        "custom",
    }
    CATALOG: ClassVar["AiGatewayModelPricingSourceType"]
    CUSTOM: ClassVar["AiGatewayModelPricingSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelPricingSourceType.CATALOG = AiGatewayModelPricingSourceType("catalog")
AiGatewayModelPricingSourceType.CUSTOM = AiGatewayModelPricingSourceType("custom")
