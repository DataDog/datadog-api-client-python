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
    from datadog_api_client.v2.model.global_incident_settings_attributes_response import (
        GlobalIncidentSettingsAttributesResponse,
    )
    from datadog_api_client.v2.model.global_incident_settings_type import GlobalIncidentSettingsType


class GlobalIncidentSettingsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_incident_settings_attributes_response import (
            GlobalIncidentSettingsAttributesResponse,
        )
        from datadog_api_client.v2.model.global_incident_settings_type import GlobalIncidentSettingsType

        return {
            "attributes": (GlobalIncidentSettingsAttributesResponse,),
            "id": (str,),
            "type": (GlobalIncidentSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: GlobalIncidentSettingsAttributesResponse, id: str, type: GlobalIncidentSettingsType, **kwargs
    ):
        """


        :param attributes: Global incident settings attributes
        :type attributes: GlobalIncidentSettingsAttributesResponse

        :param id: The unique identifier for the global incident settings
        :type id: str

        :param type: Global incident settings resource type
        :type type: GlobalIncidentSettingsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
