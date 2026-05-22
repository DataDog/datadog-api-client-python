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
    from datadog_api_client.v2.model.incident_timeline_entry_data_response import IncidentTimelineEntryDataResponse


class IncidentTimelineEntryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_entry_data_response import IncidentTimelineEntryDataResponse

        return {
            "data": (IncidentTimelineEntryDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentTimelineEntryDataResponse, **kwargs):
        """
        Response with a single timeline entry.

        :param data: Timeline entry data in a response.
        :type data: IncidentTimelineEntryDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
