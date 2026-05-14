# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTimelineEntryType(ModelSimple):
    """
    Incident timeline entry resource type.

    :param value: If omitted defaults to "incident_timeline_cells". Must be one of ["incident_timeline_cells"].
    :type value: str
    """

    allowed_values = {
        "incident_timeline_cells",
    }
    INCIDENT_TIMELINE_CELLS: ClassVar["IncidentTimelineEntryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTimelineEntryType.INCIDENT_TIMELINE_CELLS = IncidentTimelineEntryType("incident_timeline_cells")
