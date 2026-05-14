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
    from datadog_api_client.v2.model.incident_communication_data_attributes_request import (
        IncidentCommunicationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_communication_type import IncidentCommunicationType


class IncidentCommunicationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_communication_data_attributes_request import (
            IncidentCommunicationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_communication_type import IncidentCommunicationType

        return {
            "attributes": (IncidentCommunicationDataAttributesRequest,),
            "type": (IncidentCommunicationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentCommunicationDataAttributesRequest, type: IncidentCommunicationType, **kwargs
    ):
        """
        Incident communication data for a request.

        :param attributes: Attributes for creating or updating a communication.
        :type attributes: IncidentCommunicationDataAttributesRequest

        :param type: Incident communication resource type.
        :type type: IncidentCommunicationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
