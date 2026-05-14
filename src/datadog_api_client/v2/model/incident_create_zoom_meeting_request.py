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
    from datadog_api_client.v2.model.incident_create_zoom_meeting_data import IncidentCreateZoomMeetingData


class IncidentCreateZoomMeetingRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_zoom_meeting_data import IncidentCreateZoomMeetingData

        return {
            "data": (IncidentCreateZoomMeetingData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentCreateZoomMeetingData, **kwargs):
        """
        Request to create a Zoom meeting for an incident.

        :param data: Data for creating a Zoom meeting.
        :type data: IncidentCreateZoomMeetingData
        """
        super().__init__(kwargs)

        self_.data = data
