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
    from datadog_api_client.v2.model.incident_type_update_attributes import IncidentTypeUpdateAttributes
    from datadog_api_client.v2.model.incident_type_type import IncidentTypeType


class IncidentTypePatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_update_attributes import IncidentTypeUpdateAttributes
        from datadog_api_client.v2.model.incident_type_type import IncidentTypeType

        return {
            "attributes": (IncidentTypeUpdateAttributes,),
            "id": (str,),
            "type": (IncidentTypeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IncidentTypeUpdateAttributes, id: str, type: IncidentTypeType, **kwargs):
        """
        Incident type data for a patch request.

        :param attributes: Incident type's attributes for updates.
        :type attributes: IncidentTypeUpdateAttributes

        :param id: The incident type's ID.
        :type id: str

        :param type: Incident type resource type.
        :type type: IncidentTypeType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
