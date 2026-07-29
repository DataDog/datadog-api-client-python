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
    from datadog_api_client.v2.model.incident_google_meet_configuration_data_attributes_request import (
        IncidentGoogleMeetConfigurationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_google_meet_configuration_relationships_request import (
        IncidentGoogleMeetConfigurationRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_google_meet_configuration_type import IncidentGoogleMeetConfigurationType


class IncidentGoogleMeetConfigurationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_meet_configuration_data_attributes_request import (
            IncidentGoogleMeetConfigurationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_google_meet_configuration_relationships_request import (
            IncidentGoogleMeetConfigurationRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_google_meet_configuration_type import (
            IncidentGoogleMeetConfigurationType,
        )

        return {
            "attributes": (IncidentGoogleMeetConfigurationDataAttributesRequest,),
            "relationships": (IncidentGoogleMeetConfigurationRelationshipsRequest,),
            "type": (IncidentGoogleMeetConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentGoogleMeetConfigurationDataAttributesRequest,
        relationships: IncidentGoogleMeetConfigurationRelationshipsRequest,
        type: IncidentGoogleMeetConfigurationType,
        **kwargs,
    ):
        """
        Google Meet configuration data in a create request.

        :param attributes: Attributes for creating a Google Meet configuration.
        :type attributes: IncidentGoogleMeetConfigurationDataAttributesRequest

        :param relationships: Relationships for a Google Meet configuration create request.
        :type relationships: IncidentGoogleMeetConfigurationRelationshipsRequest

        :param type: Google Meet configuration resource type.
        :type type: IncidentGoogleMeetConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
