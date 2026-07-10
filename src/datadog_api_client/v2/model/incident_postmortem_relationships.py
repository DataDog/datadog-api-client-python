# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_incident import RelationshipToIncident
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.relationship_to_incident_responder import RelationshipToIncidentResponder
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser


class IncidentPostmortemRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident import RelationshipToIncident
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.relationship_to_incident_responder import RelationshipToIncidentResponder
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

        return {
            "incident": (RelationshipToIncident,),
            "last_modified_by_user": (RelationshipToUser,),
            "postmortem_owner_responder": (RelationshipToIncidentResponder,),
            "postmortem_owner_user": (NullableRelationshipToUser,),
        }

    attribute_map = {
        "incident": "incident",
        "last_modified_by_user": "last_modified_by_user",
        "postmortem_owner_responder": "postmortem_owner_responder",
        "postmortem_owner_user": "postmortem_owner_user",
    }

    def __init__(
        self_,
        incident: Union[RelationshipToIncident, UnsetType] = unset,
        last_modified_by_user: Union[RelationshipToUser, UnsetType] = unset,
        postmortem_owner_responder: Union[RelationshipToIncidentResponder, none_type, UnsetType] = unset,
        postmortem_owner_user: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The postmortem's relationships.

        :param incident: Relationship to incident.
        :type incident: RelationshipToIncident, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional

        :param postmortem_owner_responder: A relationship reference for a single incident responder.
        :type postmortem_owner_responder: RelationshipToIncidentResponder, none_type, optional

        :param postmortem_owner_user: Relationship to user.
        :type postmortem_owner_user: NullableRelationshipToUser, none_type, optional
        """
        if incident is not unset:
            kwargs["incident"] = incident
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if postmortem_owner_responder is not unset:
            kwargs["postmortem_owner_responder"] = postmortem_owner_responder
        if postmortem_owner_user is not unset:
            kwargs["postmortem_owner_user"] = postmortem_owner_user
        super().__init__(kwargs)
