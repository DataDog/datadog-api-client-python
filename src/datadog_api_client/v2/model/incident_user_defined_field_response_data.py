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
    from datadog_api_client.v2.model.incident_user_defined_field_attributes_response import (
        IncidentUserDefinedFieldAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_relationships import (
        IncidentUserDefinedFieldRelationships,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType


class IncidentUserDefinedFieldResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_attributes_response import (
            IncidentUserDefinedFieldAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_relationships import (
            IncidentUserDefinedFieldRelationships,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType

        return {
            "attributes": (IncidentUserDefinedFieldAttributesResponse,),
            "id": (str,),
            "relationships": (IncidentUserDefinedFieldRelationships,),
            "type": (IncidentUserDefinedFieldType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentUserDefinedFieldAttributesResponse,
        id: str,
        relationships: IncidentUserDefinedFieldRelationships,
        type: IncidentUserDefinedFieldType,
        **kwargs,
    ):
        """
        Data object for an incident user-defined field response.

        :param attributes: Attributes of an incident user-defined field.
        :type attributes: IncidentUserDefinedFieldAttributesResponse

        :param id: The unique identifier of the user-defined field.
        :type id: str

        :param relationships: Relationships of an incident user-defined field.
        :type relationships: IncidentUserDefinedFieldRelationships

        :param type: The incident user defined fields type.
        :type type: IncidentUserDefinedFieldType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
