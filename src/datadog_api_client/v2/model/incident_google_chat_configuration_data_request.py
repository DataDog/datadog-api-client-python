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
    from datadog_api_client.v2.model.incident_google_chat_configuration_data_attributes_request import (
        IncidentGoogleChatConfigurationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_google_chat_configuration_relationships_request import (
        IncidentGoogleChatConfigurationRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_google_chat_configuration_type import IncidentGoogleChatConfigurationType


class IncidentGoogleChatConfigurationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_chat_configuration_data_attributes_request import (
            IncidentGoogleChatConfigurationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_google_chat_configuration_relationships_request import (
            IncidentGoogleChatConfigurationRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_google_chat_configuration_type import (
            IncidentGoogleChatConfigurationType,
        )

        return {
            "attributes": (IncidentGoogleChatConfigurationDataAttributesRequest,),
            "relationships": (IncidentGoogleChatConfigurationRelationshipsRequest,),
            "type": (IncidentGoogleChatConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentGoogleChatConfigurationDataAttributesRequest,
        relationships: IncidentGoogleChatConfigurationRelationshipsRequest,
        type: IncidentGoogleChatConfigurationType,
        **kwargs,
    ):
        """
        Google Chat configuration data in a create request.

        :param attributes: Attributes for creating a Google Chat configuration.
        :type attributes: IncidentGoogleChatConfigurationDataAttributesRequest

        :param relationships: Relationships for a Google Chat configuration create request.
        :type relationships: IncidentGoogleChatConfigurationRelationshipsRequest

        :param type: Google Chat configuration resource type.
        :type type: IncidentGoogleChatConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
