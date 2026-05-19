# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AutomationRuleActionType(ModelSimple):
    """
    The type of automated action to perform when the rule triggers. `execute_workflow` runs a Datadog workflow; `assign_agent` assigns an AI agent to the case.

    :param value: Must be one of ["execute_workflow", "assign_agent"].
    :type value: str
    """

    allowed_values = {
        "execute_workflow",
        "assign_agent",
    }
    EXECUTE_WORKFLOW: ClassVar["AutomationRuleActionType"]
    ASSIGN_AGENT: ClassVar["AutomationRuleActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AutomationRuleActionType.EXECUTE_WORKFLOW = AutomationRuleActionType("execute_workflow")
AutomationRuleActionType.ASSIGN_AGENT = AutomationRuleActionType("assign_agent")
