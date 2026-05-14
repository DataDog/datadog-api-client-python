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
    from datadog_api_client.v2.model.incident_timeline_entry_data_attributes_request import (
        IncidentTimelineEntryDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_timeline_entry_type import IncidentTimelineEntryType


class IncidentTimelineEntryDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_entry_data_attributes_request import (
            IncidentTimelineEntryDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_timeline_entry_type import IncidentTimelineEntryType

        return {
            "attributes": (IncidentTimelineEntryDataAttributesRequest,),
            "type": (IncidentTimelineEntryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentTimelineEntryDataAttributesRequest, type: IncidentTimelineEntryType, **kwargs
    ):
        """
        Timeline entry data for a request.

        :param attributes: Attributes for creating or updating a timeline entry.
        :type attributes: IncidentTimelineEntryDataAttributesRequest

        :param type: Incident timeline entry resource type.
        :type type: IncidentTimelineEntryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
