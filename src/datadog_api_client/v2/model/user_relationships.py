# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles

        return {
            "roles": (RelationshipToRoles,),
        }

    attribute_map = {
        "roles": "roles",
    }

    def __init__(self, *args, **kwargs):
        """
        Relationships of the user object.

        :param roles: Relationship to roles.
        :type roles: RelationshipToRoles, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
