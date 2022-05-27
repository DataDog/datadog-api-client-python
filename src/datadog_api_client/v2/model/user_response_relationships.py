# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_organization import RelationshipToOrganization
        from datadog_api_client.v2.model.relationship_to_organizations import RelationshipToOrganizations
        from datadog_api_client.v2.model.relationship_to_users import RelationshipToUsers
        from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles

        return {
            "org": (RelationshipToOrganization,),
            "other_orgs": (RelationshipToOrganizations,),
            "other_users": (RelationshipToUsers,),
            "roles": (RelationshipToRoles,),
        }

    attribute_map = {
        "org": "org",
        "other_orgs": "other_orgs",
        "other_users": "other_users",
        "roles": "roles",
    }

    def __init__(self, *args, **kwargs):
        """
        Relationships of the user object returned by the API.

        :param org: Relationship to an organization.
        :type org: RelationshipToOrganization, optional

        :param other_orgs: Relationship to organizations.
        :type other_orgs: RelationshipToOrganizations, optional

        :param other_users: Relationship to users.
        :type other_users: RelationshipToUsers, optional

        :param roles: Relationship to roles.
        :type roles: RelationshipToRoles, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserResponseRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
