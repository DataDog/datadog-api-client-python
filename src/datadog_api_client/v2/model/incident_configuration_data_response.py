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
    from datadog_api_client.v2.model.incident_configuration_data_attributes_response import (
        IncidentConfigurationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_configuration_relationships import IncidentConfigurationRelationships
    from datadog_api_client.v2.model.incident_configuration_type import IncidentConfigurationType


class IncidentConfigurationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_configuration_data_attributes_response import (
            IncidentConfigurationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_configuration_relationships import IncidentConfigurationRelationships
        from datadog_api_client.v2.model.incident_configuration_type import IncidentConfigurationType

        return {
            "attributes": (IncidentConfigurationDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentConfigurationRelationships,),
            "type": (IncidentConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentConfigurationDataAttributesResponse,
        id: UUID,
        type: IncidentConfigurationType,
        relationships: Union[IncidentConfigurationRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident configuration data in a response.

        :param attributes: Attributes of an incident configuration in a response.
        :type attributes: IncidentConfigurationDataAttributesResponse

        :param id: The incident configuration identifier.
        :type id: UUID

        :param relationships: Relationships for an incident configuration.
        :type relationships: IncidentConfigurationRelationships, optional

        :param type: Incident configuration resource type.
        :type type: IncidentConfigurationType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
