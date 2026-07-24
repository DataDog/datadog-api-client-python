# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_ai_postmortem_data_attributes_response import (
        IncidentAIPostmortemDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_ai_postmortem_response_type import IncidentAIPostmortemResponseType


class IncidentAIPostmortemDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_ai_postmortem_data_attributes_response import (
            IncidentAIPostmortemDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_ai_postmortem_response_type import IncidentAIPostmortemResponseType

        return {
            "attributes": (IncidentAIPostmortemDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentAIPostmortemResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentAIPostmortemDataAttributesResponse,
        id: UUID,
        type: IncidentAIPostmortemResponseType,
        **kwargs,
    ):
        """
        AI postmortem data in a response.

        :param attributes: Attributes of an AI-generated incident postmortem.
        :type attributes: IncidentAIPostmortemDataAttributesResponse

        :param id: The incident identifier.
        :type id: UUID

        :param type: AI postmortem response resource type.
        :type type: IncidentAIPostmortemResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
