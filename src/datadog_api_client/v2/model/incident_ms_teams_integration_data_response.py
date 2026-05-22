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
    from datadog_api_client.v2.model.incident_ms_teams_integration_data_attributes import (
        IncidentMSTeamsIntegrationDataAttributes,
    )
    from datadog_api_client.v2.model.incident_microsoft_teams_integration_type import (
        IncidentMicrosoftTeamsIntegrationType,
    )


class IncidentMSTeamsIntegrationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_ms_teams_integration_data_attributes import (
            IncidentMSTeamsIntegrationDataAttributes,
        )
        from datadog_api_client.v2.model.incident_microsoft_teams_integration_type import (
            IncidentMicrosoftTeamsIntegrationType,
        )

        return {
            "attributes": (IncidentMSTeamsIntegrationDataAttributes,),
            "id": (UUID,),
            "type": (IncidentMicrosoftTeamsIntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentMSTeamsIntegrationDataAttributes,
        id: UUID,
        type: IncidentMicrosoftTeamsIntegrationType,
        **kwargs,
    ):
        """
        Microsoft Teams integration data in a response.

        :param attributes: Attributes of a Microsoft Teams integration metadata.
        :type attributes: IncidentMSTeamsIntegrationDataAttributes

        :param id: The integration identifier.
        :type id: UUID

        :param type: Incident integration resource type.
        :type type: IncidentMicrosoftTeamsIntegrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
