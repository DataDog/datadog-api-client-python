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
    from datadog_api_client.v2.model.incident_user_defined_field_attributes_update_request import (
        IncidentUserDefinedFieldAttributesUpdateRequest,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType


class IncidentUserDefinedFieldUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_attributes_update_request import (
            IncidentUserDefinedFieldAttributesUpdateRequest,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType

        return {
            "attributes": (IncidentUserDefinedFieldAttributesUpdateRequest,),
            "id": (str,),
            "type": (IncidentUserDefinedFieldType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentUserDefinedFieldAttributesUpdateRequest,
        id: str,
        type: IncidentUserDefinedFieldType,
        **kwargs,
    ):
        """
        Data for updating an incident user-defined field.

        :param attributes: Attributes for updating an incident user-defined field. All fields are optional.
        :type attributes: IncidentUserDefinedFieldAttributesUpdateRequest

        :param id: The unique identifier of the user-defined field to update.
        :type id: str

        :param type: The incident user defined fields type.
        :type type: IncidentUserDefinedFieldType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
