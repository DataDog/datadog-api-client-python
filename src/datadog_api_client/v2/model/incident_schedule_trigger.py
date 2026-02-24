# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_condition import IncidentCondition


class IncidentScheduleTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_condition import IncidentCondition

        return {
            "incident_type": (str,),
            "rrule": (str,),
            "tag_condition": (IncidentCondition,),
        }

    attribute_map = {
        "incident_type": "incidentType",
        "rrule": "rrule",
        "tag_condition": "tagCondition",
    }

    def __init__(
        self_,
        rrule: str,
        incident_type: Union[str, UnsetType] = unset,
        tag_condition: Union[IncidentCondition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Trigger a workflow from an Incident Schedule. The workflow must be published.

        :param incident_type: Incident type filter for the schedule.
        :type incident_type: str, optional

        :param rrule: Recurrence rule expression for scheduling.
        :type rrule: str

        :param tag_condition: A condition evaluated against incident tags.
        :type tag_condition: IncidentCondition, optional
        """
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if tag_condition is not unset:
            kwargs["tag_condition"] = tag_condition
        super().__init__(kwargs)

        self_.rrule = rrule
