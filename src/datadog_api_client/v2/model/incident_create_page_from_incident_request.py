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
    from datadog_api_client.v2.model.incident_create_page_from_incident_data_request import (
        IncidentCreatePageFromIncidentDataRequest,
    )


class IncidentCreatePageFromIncidentRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_page_from_incident_data_request import (
            IncidentCreatePageFromIncidentDataRequest,
        )

        return {
            "data": (IncidentCreatePageFromIncidentDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentCreatePageFromIncidentDataRequest, **kwargs):
        """
        Request payload for creating a page from an incident.

        :param data: Page data in a create request.
        :type data: IncidentCreatePageFromIncidentDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
