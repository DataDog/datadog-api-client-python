# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Permission(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.permission_attributes import PermissionAttributes
        from datadog_api_client.v2.model.permissions_type import PermissionsType

        return {
            "attributes": (PermissionAttributes,),
            "id": (str,),
            "type": (PermissionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Permission object.

        :param attributes: Attributes of a permission.
        :type attributes: PermissionAttributes, optional

        :param id: ID of the permission.
        :type id: str, optional

        :param type: Permissions resource type.
        :type type: PermissionsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Permission, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
