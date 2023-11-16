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
    from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType


class RelationshipToIncidentUserDefinedFieldData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType

        return {
            "id": (str,),
            "type": (IncidentUserDefinedFieldType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: IncidentUserDefinedFieldType, **kwargs):
        """
        Relationship to impact object.

        :param id: A unique identifier that represents the responder.
        :type id: str

        :param type: The incident user defined fields type.
        :type type: IncidentUserDefinedFieldType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
