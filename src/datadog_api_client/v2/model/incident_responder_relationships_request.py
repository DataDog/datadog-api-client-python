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
    from datadog_api_client.v2.model.incident_responder_user_relationship import IncidentResponderUserRelationship


class IncidentResponderRelationshipsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_user_relationship import IncidentResponderUserRelationship

        return {
            "user": (IncidentResponderUserRelationship,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(self_, user: IncidentResponderUserRelationship, **kwargs):
        """
        Relationships for creating an incident responder.

        :param user: Relationship to a user for a responder create request.
        :type user: IncidentResponderUserRelationship
        """
        super().__init__(kwargs)

        self_.user = user
