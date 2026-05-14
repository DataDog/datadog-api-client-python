# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_zoom_meeting import IncidentZoomMeeting


class IncidentZoomIntegrationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_zoom_meeting import IncidentZoomMeeting

        return {
            "created": (datetime,),
            "integration_type": (str,),
            "meetings": ([IncidentZoomMeeting],),
            "modified": (datetime,),
            "status": (str,),
        }

    attribute_map = {
        "created": "created",
        "integration_type": "integration_type",
        "meetings": "meetings",
        "modified": "modified",
        "status": "status",
    }

    def __init__(
        self_,
        created: datetime,
        integration_type: str,
        meetings: List[IncidentZoomMeeting],
        modified: datetime,
        status: str,
        **kwargs,
    ):
        """
        Attributes of a Zoom integration metadata.

        :param created: Timestamp when the integration was created.
        :type created: datetime

        :param integration_type: The type of integration.
        :type integration_type: str

        :param meetings: List of Zoom meetings.
        :type meetings: [IncidentZoomMeeting]

        :param modified: Timestamp when the integration was last modified.
        :type modified: datetime

        :param status: The status of the integration.
        :type status: str
        """
        super().__init__(kwargs)

        self_.created = created
        self_.integration_type = integration_type
        self_.meetings = meetings
        self_.modified = modified
        self_.status = status
