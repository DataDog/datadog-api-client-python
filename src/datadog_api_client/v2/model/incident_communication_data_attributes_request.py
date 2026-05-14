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
    from datadog_api_client.v2.model.incident_communication_kind import IncidentCommunicationKind
    from datadog_api_client.v2.model.incident_communication_content import IncidentCommunicationContent


class IncidentCommunicationDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_communication_kind import IncidentCommunicationKind
        from datadog_api_client.v2.model.incident_communication_content import IncidentCommunicationContent

        return {
            "communication_type": (IncidentCommunicationKind,),
            "content": (IncidentCommunicationContent,),
        }

    attribute_map = {
        "communication_type": "communication_type",
        "content": "content",
    }

    def __init__(self_, communication_type: IncidentCommunicationKind, content: IncidentCommunicationContent, **kwargs):
        """
        Attributes for creating or updating a communication.

        :param communication_type: The kind of communication.
        :type communication_type: IncidentCommunicationKind

        :param content: The content of a communication.
        :type content: IncidentCommunicationContent
        """
        super().__init__(kwargs)

        self_.communication_type = communication_type
        self_.content = content
