# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.organization import Organization
    from datadog_api_client.v2.model.permission import Permission
    from datadog_api_client.v2.model.role import Role

    globals()["Organization"] = Organization
    globals()["Permission"] = Permission
    globals()["Role"] = Role


class UserResponseIncludedItem(ModelComposed):

    validations = {}

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """
        An object related to a user.

        :param attributes: Attributes of the organization.
        :type attributes: OrganizationAttributes, optional

        :param id: ID of the organization.
        :type id: str, optional

        :param type: Organizations resource type.
        :type type: OrganizationsType

        :param relationships: Relationships of the role object returned by the API.
        :type relationships: RoleResponseRelationships, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserResponseIncludedItem, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                Organization,
                Permission,
                Role,
            ],
        }
