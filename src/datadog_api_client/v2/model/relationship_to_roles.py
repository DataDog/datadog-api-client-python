# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData

    globals()["RelationshipToRoleData"] = RelationshipToRoleData


class RelationshipToRoles(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": ([RelationshipToRoleData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        Relationship to roles.

        :param data: An array containing type and the unique identifier of a role.
        :type data: [RelationshipToRoleData], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToRoles, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
