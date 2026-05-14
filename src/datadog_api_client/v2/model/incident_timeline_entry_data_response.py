# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timeline_entry_data_attributes_response import (
        IncidentTimelineEntryDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_timeline_entry_type import IncidentTimelineEntryType


class IncidentTimelineEntryDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_entry_data_attributes_response import (
            IncidentTimelineEntryDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_timeline_entry_type import IncidentTimelineEntryType

        return {
            "attributes": (IncidentTimelineEntryDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentTimelineEntryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentTimelineEntryDataAttributesResponse,
        id: UUID,
        type: IncidentTimelineEntryType,
        **kwargs,
    ):
        """
        Timeline entry data in a response.

        :param attributes: Attributes of a timeline entry.
        :type attributes: IncidentTimelineEntryDataAttributesResponse

        :param id: The timeline entry identifier.
        :type id: UUID

        :param type: Incident timeline entry resource type.
        :type type: IncidentTimelineEntryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
