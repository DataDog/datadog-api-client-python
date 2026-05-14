# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleExecutionStateType(ModelSimple):
    """
    Incident rule execution state resource type.

    :param value: If omitted defaults to "incident_rule_execution_states". Must be one of ["incident_rule_execution_states"].
    :type value: str
    """

    allowed_values = {
        "incident_rule_execution_states",
    }
    INCIDENT_RULE_EXECUTION_STATES: ClassVar["IncidentRuleExecutionStateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRuleExecutionStateType.INCIDENT_RULE_EXECUTION_STATES = IncidentRuleExecutionStateType(
    "incident_rule_execution_states"
)
