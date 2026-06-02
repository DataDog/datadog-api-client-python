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
    from datadog_api_client.v2.model.incident_org_settings_data_attributes_response import (
        IncidentOrgSettingsDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_org_settings_relationships import IncidentOrgSettingsRelationships
    from datadog_api_client.v2.model.incident_org_settings_type import IncidentOrgSettingsType


class IncidentOrgSettingsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_org_settings_data_attributes_response import (
            IncidentOrgSettingsDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_org_settings_relationships import IncidentOrgSettingsRelationships
        from datadog_api_client.v2.model.incident_org_settings_type import IncidentOrgSettingsType

        return {
            "attributes": (IncidentOrgSettingsDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentOrgSettingsRelationships,),
            "type": (IncidentOrgSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentOrgSettingsDataAttributesResponse,
        id: UUID,
        type: IncidentOrgSettingsType,
        relationships: Union[IncidentOrgSettingsRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident org settings data in a response.

        :param attributes: Attributes of an incident org settings resource in a response.
        :type attributes: IncidentOrgSettingsDataAttributesResponse

        :param id: The org settings identifier.
        :type id: UUID

        :param relationships: Relationships for an incident org settings resource.
        :type relationships: IncidentOrgSettingsRelationships, optional

        :param type: Incident org settings resource type.
        :type type: IncidentOrgSettingsType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
