# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_pricing_request_attributes import (
        AiGatewayModelPricingRequestAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_model_pricing_type import AiGatewayModelPricingType


class AiGatewayModelPricingRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_request_attributes import (
            AiGatewayModelPricingRequestAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_type import AiGatewayModelPricingType

        return {
            "attributes": (AiGatewayModelPricingRequestAttributes,),
            "id": (str,),
            "type": (AiGatewayModelPricingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayModelPricingRequestAttributes, id: str, type: AiGatewayModelPricingType, **kwargs
    ):
        """
        Data for a model pricing request.

        :param attributes: Attributes for a model pricing request.
        :type attributes: AiGatewayModelPricingRequestAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Model pricing resource type.
        :type type: AiGatewayModelPricingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
