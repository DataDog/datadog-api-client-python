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
    from datadog_api_client.v2.model.incident_zoom_configuration_data_attributes_response import (
        IncidentZoomConfigurationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_zoom_configuration_type import IncidentZoomConfigurationType


class IncidentZoomConfigurationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_zoom_configuration_data_attributes_response import (
            IncidentZoomConfigurationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_zoom_configuration_type import IncidentZoomConfigurationType

        return {
            "attributes": (IncidentZoomConfigurationDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentZoomConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentZoomConfigurationDataAttributesResponse,
        id: UUID,
        type: IncidentZoomConfigurationType,
        **kwargs,
    ):
        """
        Zoom configuration data in a response.

        :param attributes: Attributes of a Zoom configuration.
        :type attributes: IncidentZoomConfigurationDataAttributesResponse

        :param id: The configuration identifier.
        :type id: UUID

        :param type: Zoom configuration resource type.
        :type type: IncidentZoomConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
