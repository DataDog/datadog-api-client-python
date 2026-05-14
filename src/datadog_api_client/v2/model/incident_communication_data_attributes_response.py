# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_communication_kind import IncidentCommunicationKind
    from datadog_api_client.v2.model.incident_communication_content import IncidentCommunicationContent


class IncidentCommunicationDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_communication_kind import IncidentCommunicationKind
        from datadog_api_client.v2.model.incident_communication_content import IncidentCommunicationContent

        return {
            "communication_type": (IncidentCommunicationKind,),
            "content": (IncidentCommunicationContent,),
            "created": (datetime,),
            "incident_id": (UUID,),
            "modified": (datetime,),
        }

    attribute_map = {
        "communication_type": "communication_type",
        "content": "content",
        "created": "created",
        "incident_id": "incident_id",
        "modified": "modified",
    }

    def __init__(
        self_,
        communication_type: IncidentCommunicationKind,
        content: IncidentCommunicationContent,
        created: datetime,
        incident_id: UUID,
        modified: datetime,
        **kwargs,
    ):
        """
        Attributes of an incident communication response.

        :param communication_type: The kind of communication.
        :type communication_type: IncidentCommunicationKind

        :param content: The content of a communication.
        :type content: IncidentCommunicationContent

        :param created: Timestamp when the communication was created.
        :type created: datetime

        :param incident_id: The incident identifier.
        :type incident_id: UUID

        :param modified: Timestamp when the communication was last modified.
        :type modified: datetime
        """
        super().__init__(kwargs)

        self_.communication_type = communication_type
        self_.content = content
        self_.created = created
        self_.incident_id = incident_id
        self_.modified = modified
