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
    from datadog_api_client.v2.model.incident_google_meet_integration_data_attributes import (
        IncidentGoogleMeetIntegrationDataAttributes,
    )
    from datadog_api_client.v2.model.incident_google_meet_integration_type import IncidentGoogleMeetIntegrationType


class IncidentGoogleMeetIntegrationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_meet_integration_data_attributes import (
            IncidentGoogleMeetIntegrationDataAttributes,
        )
        from datadog_api_client.v2.model.incident_google_meet_integration_type import IncidentGoogleMeetIntegrationType

        return {
            "attributes": (IncidentGoogleMeetIntegrationDataAttributes,),
            "id": (UUID,),
            "type": (IncidentGoogleMeetIntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentGoogleMeetIntegrationDataAttributes,
        id: UUID,
        type: IncidentGoogleMeetIntegrationType,
        **kwargs,
    ):
        """
        Google Meet integration data in a response.

        :param attributes: Attributes of a Google Meet integration metadata.
        :type attributes: IncidentGoogleMeetIntegrationDataAttributes

        :param id: The integration identifier.
        :type id: UUID

        :param type: Incident integration resource type.
        :type type: IncidentGoogleMeetIntegrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
