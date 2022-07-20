# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RoleUpdateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
        from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
        from datadog_api_client.v2.model.roles_type import RolesType

        return {
            "attributes": (RoleUpdateAttributes,),
            "id": (str,),
            "relationships": (RoleResponseRelationships,),
            "type": (RolesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Role object returned by the API.

        :param attributes: Attributes of the role.
        :type attributes: RoleUpdateAttributes, optional

        :param id: The unique identifier of the role.
        :type id: str, optional

        :param relationships: Relationships of the role object returned by the API.
        :type relationships: RoleResponseRelationships, optional

        :param type: Roles type.
        :type type: RolesType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleUpdateResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
