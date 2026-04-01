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
    from datadog_api_client.v2.model.incident_user_defined_field_attributes_create_request import (
        IncidentUserDefinedFieldAttributesCreateRequest,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_create_relationships import (
        IncidentUserDefinedFieldCreateRelationships,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType


class IncidentUserDefinedFieldCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_attributes_create_request import (
            IncidentUserDefinedFieldAttributesCreateRequest,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_create_relationships import (
            IncidentUserDefinedFieldCreateRelationships,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType

        return {
            "attributes": (IncidentUserDefinedFieldAttributesCreateRequest,),
            "relationships": (IncidentUserDefinedFieldCreateRelationships,),
            "type": (IncidentUserDefinedFieldType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentUserDefinedFieldAttributesCreateRequest,
        relationships: IncidentUserDefinedFieldCreateRelationships,
        type: IncidentUserDefinedFieldType,
        **kwargs,
    ):
        """
        Data for creating an incident user-defined field.

        :param attributes: Attributes for creating an incident user-defined field.
        :type attributes: IncidentUserDefinedFieldAttributesCreateRequest

        :param relationships: Relationships for creating an incident user-defined field.
        :type relationships: IncidentUserDefinedFieldCreateRelationships

        :param type: The incident user defined fields type.
        :type type: IncidentUserDefinedFieldType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
