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
    from datadog_api_client.v2.model.incident_postmortem_updated_trigger import IncidentPostmortemUpdatedTrigger


class IncidentPostmortemUpdatedTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_postmortem_updated_trigger import IncidentPostmortemUpdatedTrigger

        return {
            "incident_postmortem_updated_trigger": (IncidentPostmortemUpdatedTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "incident_postmortem_updated_trigger": "incidentPostmortemUpdatedTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_,
        incident_postmortem_updated_trigger: IncidentPostmortemUpdatedTrigger,
        start_step_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for an incident postmortem updated trigger.

        :param incident_postmortem_updated_trigger: Trigger a workflow when a postmortem is updated for an incident.
        :type incident_postmortem_updated_trigger: IncidentPostmortemUpdatedTrigger

        :param start_step_names: Names of existing workflow steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.incident_postmortem_updated_trigger = incident_postmortem_updated_trigger
