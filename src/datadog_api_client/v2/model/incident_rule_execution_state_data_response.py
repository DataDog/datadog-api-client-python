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
    from datadog_api_client.v2.model.incident_rule_execution_state_data_attributes_response import (
        IncidentRuleExecutionStateDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_rule_execution_state_type import IncidentRuleExecutionStateType


class IncidentRuleExecutionStateDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_execution_state_data_attributes_response import (
            IncidentRuleExecutionStateDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_rule_execution_state_type import IncidentRuleExecutionStateType

        return {
            "attributes": (IncidentRuleExecutionStateDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentRuleExecutionStateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentRuleExecutionStateDataAttributesResponse,
        id: UUID,
        type: IncidentRuleExecutionStateType,
        **kwargs,
    ):
        """
        Rule execution state data in a response.

        :param attributes: Attributes of an incident rule execution state.
        :type attributes: IncidentRuleExecutionStateDataAttributesResponse

        :param id: The rule execution state identifier.
        :type id: UUID

        :param type: Incident rule execution state resource type.
        :type type: IncidentRuleExecutionStateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
