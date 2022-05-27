# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RoleResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions

        return {
            "permissions": (RelationshipToPermissions,),
        }

    attribute_map = {
        "permissions": "permissions",
    }

    def __init__(self, *args, **kwargs):
        """
        Relationships of the role object returned by the API.

        :param permissions: Relationship to multiple permissions objects.
        :type permissions: RelationshipToPermissions, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleResponseRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
