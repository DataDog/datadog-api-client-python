# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TriggerWorkflowAutomationActionType(ModelSimple):
    """
    Indicates that the action triggers a Workflow Automation.

    :param value: If omitted defaults to "workflow". Must be one of ["workflow"].
    :type value: str
    """

    allowed_values = {
        "workflow",
    }
    TRIGGER_WORKFLOW_AUTOMATION: ClassVar["TriggerWorkflowAutomationActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TriggerWorkflowAutomationActionType.TRIGGER_WORKFLOW_AUTOMATION = TriggerWorkflowAutomationActionType("workflow")
