# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_type_relationships_zoom_configuration_data import (
        IncidentTypeRelationshipsZoomConfigurationData,
    )


class IncidentTypeRelationshipsZoomConfiguration(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_relationships_zoom_configuration_data import (
            IncidentTypeRelationshipsZoomConfigurationData,
        )

        return {
            "data": (IncidentTypeRelationshipsZoomConfigurationData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[IncidentTypeRelationshipsZoomConfigurationData, none_type], **kwargs):
        """
        The definition of ``IncidentTypeRelationshipsZoomConfiguration`` object.

        :param data: The Zoom configuration relationship data object.
        :type data: IncidentTypeRelationshipsZoomConfigurationData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
