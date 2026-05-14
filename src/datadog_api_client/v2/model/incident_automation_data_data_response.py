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
    from datadog_api_client.v2.model.incident_automation_data_attributes_response import (
        IncidentAutomationDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_automation_data_type import IncidentAutomationDataType


class IncidentAutomationDataDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_automation_data_attributes_response import (
            IncidentAutomationDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_automation_data_type import IncidentAutomationDataType

        return {
            "attributes": (IncidentAutomationDataAttributesResponse,),
            "id": (str,),
            "type": (IncidentAutomationDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentAutomationDataAttributesResponse, id: str, type: IncidentAutomationDataType, **kwargs
    ):
        """
        Automation data in a response.

        :param attributes: Attributes of incident automation data.
        :type attributes: IncidentAutomationDataAttributesResponse

        :param id: The automation data identifier.
        :type id: str

        :param type: Incident automation data resource type.
        :type type: IncidentAutomationDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
