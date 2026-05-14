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
    from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_attributes_response import (
        IncidentMicrosoftTeamsConfigurationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_microsoft_teams_configuration_type import (
        IncidentMicrosoftTeamsConfigurationType,
    )


class IncidentMicrosoftTeamsConfigurationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_attributes_response import (
            IncidentMicrosoftTeamsConfigurationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_microsoft_teams_configuration_type import (
            IncidentMicrosoftTeamsConfigurationType,
        )

        return {
            "attributes": (IncidentMicrosoftTeamsConfigurationDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentMicrosoftTeamsConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentMicrosoftTeamsConfigurationDataAttributesResponse,
        id: UUID,
        type: IncidentMicrosoftTeamsConfigurationType,
        **kwargs,
    ):
        """
        Microsoft Teams configuration data in a response.

        :param attributes: Attributes of a Microsoft Teams configuration.
        :type attributes: IncidentMicrosoftTeamsConfigurationDataAttributesResponse

        :param id: The configuration identifier.
        :type id: UUID

        :param type: Microsoft Teams configuration resource type.
        :type type: IncidentMicrosoftTeamsConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
