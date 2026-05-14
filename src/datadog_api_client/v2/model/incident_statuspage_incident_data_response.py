# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_statuspage_incident_data_attributes_response import (
        IncidentStatuspageIncidentDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_statuspage_incident_type import IncidentStatuspageIncidentType


class IncidentStatuspageIncidentDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_incident_data_attributes_response import (
            IncidentStatuspageIncidentDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_statuspage_incident_type import IncidentStatuspageIncidentType

        return {
            "attributes": (IncidentStatuspageIncidentDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentStatuspageIncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatuspageIncidentDataAttributesResponse,
        id: UUID,
        type: IncidentStatuspageIncidentType,
        **kwargs,
    ):
        """
        Statuspage incident data in a response.

        :param attributes: Attributes of a Statuspage incident integration.
        :type attributes: IncidentStatuspageIncidentDataAttributesResponse

        :param id: The integration identifier.
        :type id: UUID

        :param type: Statuspage incident integration resource type.
        :type type: IncidentStatuspageIncidentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
