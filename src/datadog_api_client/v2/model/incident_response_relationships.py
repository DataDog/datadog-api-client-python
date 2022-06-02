# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.relationship_to_incident_integration_metadatas import (
            RelationshipToIncidentIntegrationMetadatas,
        )
        from datadog_api_client.v2.model.relationship_to_incident_postmortem import RelationshipToIncidentPostmortem

        return {
            "commander_user": (NullableRelationshipToUser,),
            "created_by_user": (RelationshipToUser,),
            "integrations": (RelationshipToIncidentIntegrationMetadatas,),
            "last_modified_by_user": (RelationshipToUser,),
            "postmortem": (RelationshipToIncidentPostmortem,),
        }

    attribute_map = {
        "commander_user": "commander_user",
        "created_by_user": "created_by_user",
        "integrations": "integrations",
        "last_modified_by_user": "last_modified_by_user",
        "postmortem": "postmortem",
    }

    def __init__(self, *args, **kwargs):
        """
        The incident's relationships from a response.

        :param commander_user: Relationship to user.
        :type commander_user: NullableRelationshipToUser, optional

        :param created_by_user: Relationship to user.
        :type created_by_user: RelationshipToUser, optional

        :param integrations: A relationship reference for multiple integration metadata objects.
        :type integrations: RelationshipToIncidentIntegrationMetadatas, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional

        :param postmortem: A relationship reference for postmortems.
        :type postmortem: RelationshipToIncidentPostmortem, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentResponseRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
