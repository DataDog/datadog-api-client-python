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
    from datadog_api_client.v2.model.relationship_to_incident_attachment import RelationshipToIncidentAttachment
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.relationship_to_incident_impacts import RelationshipToIncidentImpacts
    from datadog_api_client.v2.model.relationship_to_incident_integration_metadatas import (
        RelationshipToIncidentIntegrationMetadatas,
    )
    from datadog_api_client.v2.model.relationship_to_incident_responders import RelationshipToIncidentResponders
    from datadog_api_client.v2.model.relationship_to_incident_user_defined_fields import (
        RelationshipToIncidentUserDefinedFields,
    )


class IncidentResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_attachment import RelationshipToIncidentAttachment
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.relationship_to_incident_impacts import RelationshipToIncidentImpacts
        from datadog_api_client.v2.model.relationship_to_incident_integration_metadatas import (
            RelationshipToIncidentIntegrationMetadatas,
        )
        from datadog_api_client.v2.model.relationship_to_incident_responders import RelationshipToIncidentResponders
        from datadog_api_client.v2.model.relationship_to_incident_user_defined_fields import (
            RelationshipToIncidentUserDefinedFields,
        )

        return {
            "attachments": (RelationshipToIncidentAttachment,),
            "commander_user": (NullableRelationshipToUser,),
            "created_by_user": (RelationshipToUser,),
            "impacts": (RelationshipToIncidentImpacts,),
            "integrations": (RelationshipToIncidentIntegrationMetadatas,),
            "last_modified_by_user": (RelationshipToUser,),
            "responders": (RelationshipToIncidentResponders,),
            "user_defined_fields": (RelationshipToIncidentUserDefinedFields,),
        }

    attribute_map = {
        "attachments": "attachments",
        "commander_user": "commander_user",
        "created_by_user": "created_by_user",
        "impacts": "impacts",
        "integrations": "integrations",
        "last_modified_by_user": "last_modified_by_user",
        "responders": "responders",
        "user_defined_fields": "user_defined_fields",
    }

    def __init__(
        self_,
        attachments: Union[RelationshipToIncidentAttachment, UnsetType] = unset,
        commander_user: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        created_by_user: Union[RelationshipToUser, UnsetType] = unset,
        impacts: Union[RelationshipToIncidentImpacts, UnsetType] = unset,
        integrations: Union[RelationshipToIncidentIntegrationMetadatas, UnsetType] = unset,
        last_modified_by_user: Union[RelationshipToUser, UnsetType] = unset,
        responders: Union[RelationshipToIncidentResponders, UnsetType] = unset,
        user_defined_fields: Union[RelationshipToIncidentUserDefinedFields, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident's relationships from a response.

        :param attachments: A relationship reference for attachments.
        :type attachments: RelationshipToIncidentAttachment, optional

        :param commander_user: Relationship to user.
        :type commander_user: NullableRelationshipToUser, none_type, optional

        :param created_by_user: Relationship to user.
        :type created_by_user: RelationshipToUser, optional

        :param impacts: Relationship to impacts.
        :type impacts: RelationshipToIncidentImpacts, optional

        :param integrations: A relationship reference for multiple integration metadata objects.
        :type integrations: RelationshipToIncidentIntegrationMetadatas, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional

        :param responders: Relationship to incident responders.
        :type responders: RelationshipToIncidentResponders, optional

        :param user_defined_fields: Relationship to incident user defined fields.
        :type user_defined_fields: RelationshipToIncidentUserDefinedFields, optional
        """
        if attachments is not unset:
            kwargs["attachments"] = attachments
        if commander_user is not unset:
            kwargs["commander_user"] = commander_user
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if impacts is not unset:
            kwargs["impacts"] = impacts
        if integrations is not unset:
            kwargs["integrations"] = integrations
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if responders is not unset:
            kwargs["responders"] = responders
        if user_defined_fields is not unset:
            kwargs["user_defined_fields"] = user_defined_fields
        super().__init__(kwargs)
