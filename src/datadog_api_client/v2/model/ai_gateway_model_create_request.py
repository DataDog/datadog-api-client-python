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
    from datadog_api_client.v2.model.ai_gateway_model_create_data import AiGatewayModelCreateData


class AiGatewayModelCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_create_data import AiGatewayModelCreateData

        return {
            "data": (AiGatewayModelCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayModelCreateData, **kwargs):
        """
        Request to create a model catalog entry.

        :param data: Data used to create a model catalog entry.
        :type data: AiGatewayModelCreateData
        """
        super().__init__(kwargs)

        self_.data = data
