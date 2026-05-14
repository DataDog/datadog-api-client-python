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
    from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data_attributes import (
        IncidentBatchCreateRuleExecutionStatesDataAttributes,
    )
    from datadog_api_client.v2.model.incident_rule_execution_state_type import IncidentRuleExecutionStateType


class IncidentBatchCreateRuleExecutionStatesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data_attributes import (
            IncidentBatchCreateRuleExecutionStatesDataAttributes,
        )
        from datadog_api_client.v2.model.incident_rule_execution_state_type import IncidentRuleExecutionStateType

        return {
            "attributes": (IncidentBatchCreateRuleExecutionStatesDataAttributes,),
            "type": (IncidentRuleExecutionStateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentBatchCreateRuleExecutionStatesDataAttributes,
        type: IncidentRuleExecutionStateType,
        **kwargs,
    ):
        """
        Data for batch creating rule execution states.

        :param attributes: Attributes for batch creating rule execution states.
        :type attributes: IncidentBatchCreateRuleExecutionStatesDataAttributes

        :param type: Incident rule execution state resource type.
        :type type: IncidentRuleExecutionStateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
