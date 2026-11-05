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
    from datadog_api_client.v2.model.ai_gateway_governance_attributes import AiGatewayGovernanceAttributes
    from datadog_api_client.v2.model.ai_gateway_governance_type import AiGatewayGovernanceType


class AiGatewayGovernanceResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_governance_attributes import AiGatewayGovernanceAttributes
        from datadog_api_client.v2.model.ai_gateway_governance_type import AiGatewayGovernanceType

        return {
            "attributes": (AiGatewayGovernanceAttributes,),
            "id": (str,),
            "type": (AiGatewayGovernanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayGovernanceAttributes, id: str, type: AiGatewayGovernanceType, **kwargs):
        """
        Organization-wide AI Gateway governance resource.

        :param attributes: Organization-wide AI Gateway governance controls.
        :type attributes: AiGatewayGovernanceAttributes

        :param id: Singleton governance resource identifier.
        :type id: str

        :param type: AI Gateway governance resource type.
        :type type: AiGatewayGovernanceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
