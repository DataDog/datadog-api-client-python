# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_governance_replace_attributes import (
        AiGatewayGovernanceReplaceAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_governance_type import AiGatewayGovernanceType


class AiGatewayGovernanceReplaceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_governance_replace_attributes import (
            AiGatewayGovernanceReplaceAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_governance_type import AiGatewayGovernanceType

        return {
            "attributes": (AiGatewayGovernanceReplaceAttributes,),
            "id": (str,),
            "type": (AiGatewayGovernanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayGovernanceReplaceAttributes,
        type: AiGatewayGovernanceType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data used to replace the organization's AI Gateway governance controls.

        :param attributes: Organization-wide AI Gateway governance controls to replace.
        :type attributes: AiGatewayGovernanceReplaceAttributes

        :param id: Optional singleton governance resource identifier. When provided, it must be ``organization``.
        :type id: str, optional

        :param type: AI Gateway governance resource type.
        :type type: AiGatewayGovernanceType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
