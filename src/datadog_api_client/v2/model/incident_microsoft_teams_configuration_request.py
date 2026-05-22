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
    from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_request import (
        IncidentMicrosoftTeamsConfigurationDataRequest,
    )


class IncidentMicrosoftTeamsConfigurationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_request import (
            IncidentMicrosoftTeamsConfigurationDataRequest,
        )

        return {
            "data": (IncidentMicrosoftTeamsConfigurationDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentMicrosoftTeamsConfigurationDataRequest, **kwargs):
        """
        Request to create or update a Microsoft Teams configuration.

        :param data: Microsoft Teams configuration data for a request.
        :type data: IncidentMicrosoftTeamsConfigurationDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
