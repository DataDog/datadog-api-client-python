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
    from datadog_api_client.v2.model.incident_status_pages_suggestion_data import IncidentStatusPagesSuggestionData


class IncidentStatusPagesSuggestionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_status_pages_suggestion_data import IncidentStatusPagesSuggestionData

        return {
            "data": (IncidentStatusPagesSuggestionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentStatusPagesSuggestionData, **kwargs):
        """
        Response with a status pages suggestion.

        :param data: Status pages suggestion data.
        :type data: IncidentStatusPagesSuggestionData
        """
        super().__init__(kwargs)

        self_.data = data
