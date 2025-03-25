# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_trigger import MonitorTrigger


class MonitorTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_trigger import MonitorTrigger

        return {
            "monitor_trigger": (MonitorTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "monitor_trigger": "monitorTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_, monitor_trigger: MonitorTrigger, start_step_names: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Schema for a Monitor-based trigger.

        :param monitor_trigger: Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
        :type monitor_trigger: MonitorTrigger

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.monitor_trigger = monitor_trigger
