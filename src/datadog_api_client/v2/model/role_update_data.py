# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
    from datadog_api_client.v2.model.roles_type import RolesType

    globals()["RoleUpdateAttributes"] = RoleUpdateAttributes
    globals()["RolesType"] = RolesType


class RoleUpdateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (RoleUpdateAttributes,),
            "id": (str,),
            "type": (RolesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        Data related to the update of a role.

        :param attributes: Attributes of the role.
        :type attributes: RoleUpdateAttributes

        :param id: ID of the role.
        :type id: str

        :param type: Roles type.
        :type type: RolesType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
