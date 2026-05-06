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
    from datadog_api_client.v2.model.trigger_workflow_automation_action_type import TriggerWorkflowAutomationActionType


class TriggerWorkflowAutomationAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_workflow_automation_action_type import (
            TriggerWorkflowAutomationActionType,
        )

        return {
            "handle": (str,),
            "type": (TriggerWorkflowAutomationActionType,),
        }

    attribute_map = {
        "handle": "handle",
        "type": "type",
    }

    def __init__(self_, handle: str, type: TriggerWorkflowAutomationActionType, **kwargs):
        """
        Triggers a Workflow Automation.

        :param handle: The handle of the Workflow Automation to trigger.
        :type handle: str

        :param type: Indicates that the action triggers a Workflow Automation.
        :type type: TriggerWorkflowAutomationActionType
        """
        super().__init__(kwargs)

        self_.handle = handle
        self_.type = type
