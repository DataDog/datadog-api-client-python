# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_google_meet_configuration_data_attributes_response import (
        IncidentGoogleMeetConfigurationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_google_meet_configuration_relationships import (
        IncidentGoogleMeetConfigurationRelationships,
    )
    from datadog_api_client.v2.model.incident_google_meet_configuration_type import IncidentGoogleMeetConfigurationType


class IncidentGoogleMeetConfigurationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_meet_configuration_data_attributes_response import (
            IncidentGoogleMeetConfigurationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_google_meet_configuration_relationships import (
            IncidentGoogleMeetConfigurationRelationships,
        )
        from datadog_api_client.v2.model.incident_google_meet_configuration_type import (
            IncidentGoogleMeetConfigurationType,
        )

        return {
            "attributes": (IncidentGoogleMeetConfigurationDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentGoogleMeetConfigurationRelationships,),
            "type": (IncidentGoogleMeetConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentGoogleMeetConfigurationDataAttributesResponse,
        id: UUID,
        type: IncidentGoogleMeetConfigurationType,
        relationships: Union[IncidentGoogleMeetConfigurationRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Meet configuration data in a response.

        :param attributes: Attributes of a Google Meet configuration.
        :type attributes: IncidentGoogleMeetConfigurationDataAttributesResponse

        :param id: The configuration identifier.
        :type id: UUID

        :param relationships: Relationships for a Google Meet configuration.
        :type relationships: IncidentGoogleMeetConfigurationRelationships, optional

        :param type: Google Meet configuration resource type.
        :type type: IncidentGoogleMeetConfigurationType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
