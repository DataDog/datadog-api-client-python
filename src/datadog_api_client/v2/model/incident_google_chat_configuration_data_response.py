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
    from datadog_api_client.v2.model.incident_google_chat_configuration_data_attributes_response import (
        IncidentGoogleChatConfigurationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_google_chat_configuration_relationships import (
        IncidentGoogleChatConfigurationRelationships,
    )
    from datadog_api_client.v2.model.incident_google_chat_configuration_type import IncidentGoogleChatConfigurationType


class IncidentGoogleChatConfigurationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_chat_configuration_data_attributes_response import (
            IncidentGoogleChatConfigurationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_google_chat_configuration_relationships import (
            IncidentGoogleChatConfigurationRelationships,
        )
        from datadog_api_client.v2.model.incident_google_chat_configuration_type import (
            IncidentGoogleChatConfigurationType,
        )

        return {
            "attributes": (IncidentGoogleChatConfigurationDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentGoogleChatConfigurationRelationships,),
            "type": (IncidentGoogleChatConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentGoogleChatConfigurationDataAttributesResponse,
        id: UUID,
        type: IncidentGoogleChatConfigurationType,
        relationships: Union[IncidentGoogleChatConfigurationRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat configuration data in a response.

        :param attributes: Attributes of a Google Chat configuration.
        :type attributes: IncidentGoogleChatConfigurationDataAttributesResponse

        :param id: The configuration identifier.
        :type id: UUID

        :param relationships: Relationships for a Google Chat configuration.
        :type relationships: IncidentGoogleChatConfigurationRelationships, optional

        :param type: Google Chat configuration resource type.
        :type type: IncidentGoogleChatConfigurationType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
