# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_field_match import (
        AiGatewayModelAutomaticPricingFieldMatch,
    )


class AiGatewayModelAutomaticPricingModeTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_field_match import (
            AiGatewayModelAutomaticPricingFieldMatch,
        )

        return {
            "body": ([AiGatewayModelAutomaticPricingFieldMatch],),
            "headers": ([AiGatewayModelAutomaticPricingFieldMatch],),
            "mode": (str,),
        }

    attribute_map = {
        "body": "body",
        "headers": "headers",
        "mode": "mode",
    }

    def __init__(
        self_,
        mode: str,
        body: Union[List[AiGatewayModelAutomaticPricingFieldMatch], UnsetType] = unset,
        headers: Union[List[AiGatewayModelAutomaticPricingFieldMatch], UnsetType] = unset,
        **kwargs,
    ):
        """
        Request fields that select a priced mode.

        :param body: Request body fields that must match.
        :type body: [AiGatewayModelAutomaticPricingFieldMatch], optional

        :param headers: Request headers that must match.
        :type headers: [AiGatewayModelAutomaticPricingFieldMatch], optional

        :param mode: Priced mode selected by the fields.
        :type mode: str
        """
        if body is not unset:
            kwargs["body"] = body
        if headers is not unset:
            kwargs["headers"] = headers
        super().__init__(kwargs)

        self_.mode = mode
