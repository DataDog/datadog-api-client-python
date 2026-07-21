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
    from datadog_api_client.v2.model.incident_rule_data_attributes_response import IncidentRuleDataAttributesResponse
    from datadog_api_client.v2.model.incident_rule_response_type import IncidentRuleResponseType


class IncidentRuleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_data_attributes_response import (
            IncidentRuleDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_rule_response_type import IncidentRuleResponseType

        return {
            "attributes": (IncidentRuleDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentRuleResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentRuleDataAttributesResponse, id: UUID, type: IncidentRuleResponseType, **kwargs
    ):
        """
        Incident rule data in a response.

        :param attributes: Attributes of an incident rule in a response.
        :type attributes: IncidentRuleDataAttributesResponse

        :param id: The rule identifier.
        :type id: UUID

        :param type: Incident rule response resource type.
        :type type: IncidentRuleResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
