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
    from datadog_api_client.v2.model.incident_impact_updated_trigger import IncidentImpactUpdatedTrigger


class IncidentImpactUpdatedTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_updated_trigger import IncidentImpactUpdatedTrigger

        return {
            "incident_impact_updated_trigger": (IncidentImpactUpdatedTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "incident_impact_updated_trigger": "incidentImpactUpdatedTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_,
        incident_impact_updated_trigger: IncidentImpactUpdatedTrigger,
        start_step_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for an incident impact updated trigger.

        :param incident_impact_updated_trigger: Trigger a workflow when an impact is updated for an incident.
        :type incident_impact_updated_trigger: IncidentImpactUpdatedTrigger

        :param start_step_names: Names of existing workflow steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.incident_impact_updated_trigger = incident_impact_updated_trigger
