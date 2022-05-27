# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentServiceRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

        return {
            "created_by": (RelationshipToUser,),
            "last_modified_by": (RelationshipToUser,),
        }

    attribute_map = {
        "created_by": "created_by",
        "last_modified_by": "last_modified_by",
    }

    def __init__(self, *args, **kwargs):
        """
        The incident service's relationships.

        :param created_by: Relationship to user.
        :type created_by: RelationshipToUser, optional

        :param last_modified_by: Relationship to user.
        :type last_modified_by: RelationshipToUser, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentServiceRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
