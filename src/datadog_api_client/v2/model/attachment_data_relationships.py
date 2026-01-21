# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_incident import RelationshipToIncident
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser


class AttachmentDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident import RelationshipToIncident
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

        return {
            "incident": (RelationshipToIncident,),
            "last_modified_by_user": (RelationshipToUser,),
        }

    attribute_map = {
        "incident": "incident",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        incident: Union[RelationshipToIncident, UnsetType] = unset,
        last_modified_by_user: Union[RelationshipToUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attachment's resource relationships.

        :param incident: Relationship to incident.
        :type incident: RelationshipToIncident, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional
        """
        if incident is not unset:
            kwargs["incident"] = incident
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        super().__init__(kwargs)
