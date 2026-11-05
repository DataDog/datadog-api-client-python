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
    from datadog_api_client.v2.model.ai_gateway_models_by_canonical_attributes import (
        AiGatewayModelsByCanonicalAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_models_by_canonical_type import AiGatewayModelsByCanonicalType


class AiGatewayModelsByCanonicalResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_models_by_canonical_attributes import (
            AiGatewayModelsByCanonicalAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_models_by_canonical_type import AiGatewayModelsByCanonicalType

        return {
            "attributes": (AiGatewayModelsByCanonicalAttributes,),
            "id": (str,),
            "type": (AiGatewayModelsByCanonicalType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayModelsByCanonicalAttributes, id: str, type: AiGatewayModelsByCanonicalType, **kwargs
    ):
        """
        Canonical model grouping resource.

        :param attributes: Provider entries grouped under one canonical model ID.
        :type attributes: AiGatewayModelsByCanonicalAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Canonical model grouping resource type.
        :type type: AiGatewayModelsByCanonicalType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
