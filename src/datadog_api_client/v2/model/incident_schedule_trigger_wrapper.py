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
    from datadog_api_client.v2.model.incident_schedule_trigger import IncidentScheduleTrigger


class IncidentScheduleTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_schedule_trigger import IncidentScheduleTrigger

        return {
            "incident_schedule_trigger": (IncidentScheduleTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "incident_schedule_trigger": "incidentScheduleTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_,
        incident_schedule_trigger: IncidentScheduleTrigger,
        start_step_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for an Incident Schedule-based trigger.

        :param incident_schedule_trigger: Trigger a workflow from an Incident Schedule. The workflow must be published.
        :type incident_schedule_trigger: IncidentScheduleTrigger

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.incident_schedule_trigger = incident_schedule_trigger
