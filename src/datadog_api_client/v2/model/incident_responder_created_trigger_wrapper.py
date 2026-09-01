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
    from datadog_api_client.v2.model.incident_responder_created_trigger import IncidentResponderCreatedTrigger


class IncidentResponderCreatedTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_created_trigger import IncidentResponderCreatedTrigger

        return {
            "incident_responder_created_trigger": (IncidentResponderCreatedTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "incident_responder_created_trigger": "incidentResponderCreatedTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_,
        incident_responder_created_trigger: IncidentResponderCreatedTrigger,
        start_step_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for an incident responder created trigger.

        :param incident_responder_created_trigger: Trigger a workflow when a responder is created for an incident.
        :type incident_responder_created_trigger: IncidentResponderCreatedTrigger

        :param start_step_names: Names of existing workflow steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.incident_responder_created_trigger = incident_responder_created_trigger
