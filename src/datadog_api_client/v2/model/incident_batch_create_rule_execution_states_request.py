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
    from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data import (
        IncidentBatchCreateRuleExecutionStatesData,
    )


class IncidentBatchCreateRuleExecutionStatesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data import (
            IncidentBatchCreateRuleExecutionStatesData,
        )

        return {
            "data": (IncidentBatchCreateRuleExecutionStatesData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentBatchCreateRuleExecutionStatesData, **kwargs):
        """
        Request to batch create rule execution states.

        :param data: Data for batch creating rule execution states.
        :type data: IncidentBatchCreateRuleExecutionStatesData
        """
        super().__init__(kwargs)

        self_.data = data
