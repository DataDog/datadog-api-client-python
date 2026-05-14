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
    from datadog_api_client.v2.model.incident_automation_data_attributes_request import (
        IncidentAutomationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_automation_data_type import IncidentAutomationDataType


class IncidentAutomationDataDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_automation_data_attributes_request import (
            IncidentAutomationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_automation_data_type import IncidentAutomationDataType

        return {
            "attributes": (IncidentAutomationDataAttributesRequest,),
            "type": (IncidentAutomationDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentAutomationDataAttributesRequest, type: IncidentAutomationDataType, **kwargs
    ):
        """
        Automation data for a request.

        :param attributes: Attributes for upserting automation data.
        :type attributes: IncidentAutomationDataAttributesRequest

        :param type: Incident automation data resource type.
        :type type: IncidentAutomationDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
