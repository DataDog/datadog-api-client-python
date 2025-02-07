# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class WorkflowTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "start_step_names": ([str],),
            "workflow_trigger": (dict,),
        }

    attribute_map = {
        "start_step_names": "startStepNames",
        "workflow_trigger": "workflowTrigger",
    }

    def __init__(self_, workflow_trigger: dict, start_step_names: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Schema for a Workflow-based trigger.

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional

        :param workflow_trigger: Trigger a workflow VIA the Datadog UI. Only required if no other trigger exists.
        :type workflow_trigger: dict
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.workflow_trigger = workflow_trigger
