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
    from datadog_api_client.v2.model.incident_create_page_from_incident_data_attributes_request import (
        IncidentCreatePageFromIncidentDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_create_page_from_incident_type import IncidentCreatePageFromIncidentType


class IncidentCreatePageFromIncidentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_page_from_incident_data_attributes_request import (
            IncidentCreatePageFromIncidentDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_create_page_from_incident_type import (
            IncidentCreatePageFromIncidentType,
        )

        return {
            "attributes": (IncidentCreatePageFromIncidentDataAttributesRequest,),
            "type": (IncidentCreatePageFromIncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentCreatePageFromIncidentDataAttributesRequest,
        type: IncidentCreatePageFromIncidentType,
        **kwargs,
    ):
        """
        Page data in a create request.

        :param attributes: Attributes for creating a page from an incident.
        :type attributes: IncidentCreatePageFromIncidentDataAttributesRequest

        :param type: Resource type for a page creation request.
        :type type: IncidentCreatePageFromIncidentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
