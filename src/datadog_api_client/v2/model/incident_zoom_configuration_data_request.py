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
    from datadog_api_client.v2.model.incident_zoom_configuration_data_attributes_request import (
        IncidentZoomConfigurationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_zoom_configuration_type import IncidentZoomConfigurationType


class IncidentZoomConfigurationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_zoom_configuration_data_attributes_request import (
            IncidentZoomConfigurationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_zoom_configuration_type import IncidentZoomConfigurationType

        return {
            "attributes": (IncidentZoomConfigurationDataAttributesRequest,),
            "type": (IncidentZoomConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentZoomConfigurationDataAttributesRequest, type: IncidentZoomConfigurationType, **kwargs
    ):
        """
        Zoom configuration data for a request.

        :param attributes: Attributes for creating or updating a Zoom configuration.
        :type attributes: IncidentZoomConfigurationDataAttributesRequest

        :param type: Zoom configuration resource type.
        :type type: IncidentZoomConfigurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
