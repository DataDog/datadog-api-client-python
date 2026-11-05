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
    from datadog_api_client.v2.model.ai_gateway_models_bulk_create_data import AiGatewayModelsBulkCreateData


class AiGatewayModelsBulkCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_models_bulk_create_data import AiGatewayModelsBulkCreateData

        return {
            "data": (AiGatewayModelsBulkCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayModelsBulkCreateData, **kwargs):
        """
        Request to create several model catalog entries.

        :param data: Data used to create several model catalog entries.
        :type data: AiGatewayModelsBulkCreateData
        """
        super().__init__(kwargs)

        self_.data = data
