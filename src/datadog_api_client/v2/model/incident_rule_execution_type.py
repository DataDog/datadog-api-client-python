# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleExecutionType(ModelSimple):
    """
    The execution type of an incident rule.

    :param value: Must be one of [1, 2].
    :type value: int
    """

    allowed_values = {
        1,
        2,
    }
    SINGLE_EXECUTION: ClassVar["IncidentRuleExecutionType"]
    MULTI_EXECUTION: ClassVar["IncidentRuleExecutionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


IncidentRuleExecutionType.SINGLE_EXECUTION = IncidentRuleExecutionType(1)
IncidentRuleExecutionType.MULTI_EXECUTION = IncidentRuleExecutionType(2)
