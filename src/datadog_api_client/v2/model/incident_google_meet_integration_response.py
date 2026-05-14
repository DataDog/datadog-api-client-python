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
    from datadog_api_client.v2.model.incident_google_meet_integration_data_response import (
        IncidentGoogleMeetIntegrationDataResponse,
    )


class IncidentGoogleMeetIntegrationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_meet_integration_data_response import (
            IncidentGoogleMeetIntegrationDataResponse,
        )

        return {
            "data": (IncidentGoogleMeetIntegrationDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentGoogleMeetIntegrationDataResponse, **kwargs):
        """
        Response with Google Meet integration metadata.

        :param data: Google Meet integration data in a response.
        :type data: IncidentGoogleMeetIntegrationDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
