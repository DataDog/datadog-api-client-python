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
    from datadog_api_client.v2.model.incident_create_zoom_meeting_data_attributes import (
        IncidentCreateZoomMeetingDataAttributes,
    )
    from datadog_api_client.v2.model.incident_zoom_integration_type import IncidentZoomIntegrationType


class IncidentCreateZoomMeetingData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_zoom_meeting_data_attributes import (
            IncidentCreateZoomMeetingDataAttributes,
        )
        from datadog_api_client.v2.model.incident_zoom_integration_type import IncidentZoomIntegrationType

        return {
            "attributes": (IncidentCreateZoomMeetingDataAttributes,),
            "type": (IncidentZoomIntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentCreateZoomMeetingDataAttributes, type: IncidentZoomIntegrationType, **kwargs
    ):
        """
        Data for creating a Zoom meeting.

        :param attributes: Attributes for creating a Zoom meeting.
        :type attributes: IncidentCreateZoomMeetingDataAttributes

        :param type: Incident integration resource type.
        :type type: IncidentZoomIntegrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
