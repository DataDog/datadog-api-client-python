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
    from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_attributes_request import (
        IncidentMicrosoftTeamsConfigurationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_microsoft_teams_configuration_type import (
        IncidentMicrosoftTeamsConfigurationType,
    )


class IncidentMicrosoftTeamsConfigurationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_attributes_request import (
            IncidentMicrosoftTeamsConfigurationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_microsoft_teams_configuration_type import (
            IncidentMicrosoftTeamsConfigurationType,
        )

        return {
            "attributes": (IncidentMicrosoftTeamsConfigurationDataAttributesRequest,),
            "type": (IncidentMicrosoftTeamsConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentMicrosoftTeamsConfigurationDataAttributesRequest,
        type: IncidentMicrosoftTeamsConfigurationType,
        **kwargs,
    ):
        """
        Microsoft Teams configuration data for a request.

        :param attributes: Attributes for creating or updating a Microsoft Teams configuration.
        :type attributes: IncidentMicrosoftTeamsConfigurationDataAttributesRequest

        :param type: Microsoft Teams configuration resource type.
        :type type: IncidentMicrosoftTeamsConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
