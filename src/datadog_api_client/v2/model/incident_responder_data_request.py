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
    from datadog_api_client.v2.model.incident_responder_relationships_request import (
        IncidentResponderRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_responder_type import IncidentResponderType


class IncidentResponderDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_relationships_request import (
            IncidentResponderRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_responder_type import IncidentResponderType

        return {
            "relationships": (IncidentResponderRelationshipsRequest,),
            "type": (IncidentResponderType,),
        }

    attribute_map = {
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self_, relationships: IncidentResponderRelationshipsRequest, type: IncidentResponderType, **kwargs):
        """
        Incident responder data in a create request.

        :param relationships: Relationships for creating an incident responder.
        :type relationships: IncidentResponderRelationshipsRequest

        :param type: Incident responder resource type.
        :type type: IncidentResponderType
        """
        super().__init__(kwargs)

        self_.relationships = relationships
        self_.type = type
