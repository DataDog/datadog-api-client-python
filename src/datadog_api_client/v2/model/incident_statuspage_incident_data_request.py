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
    from datadog_api_client.v2.model.incident_statuspage_incident_data_attributes_request import (
        IncidentStatuspageIncidentDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_statuspage_incident_type import IncidentStatuspageIncidentType


class IncidentStatuspageIncidentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_incident_data_attributes_request import (
            IncidentStatuspageIncidentDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_statuspage_incident_type import IncidentStatuspageIncidentType

        return {
            "attributes": (IncidentStatuspageIncidentDataAttributesRequest,),
            "type": (IncidentStatuspageIncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatuspageIncidentDataAttributesRequest,
        type: IncidentStatuspageIncidentType,
        **kwargs,
    ):
        """
        Statuspage incident data for a request.

        :param attributes: Attributes for creating or updating a Statuspage incident.
        :type attributes: IncidentStatuspageIncidentDataAttributesRequest

        :param type: Statuspage incident integration resource type.
        :type type: IncidentStatuspageIncidentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
