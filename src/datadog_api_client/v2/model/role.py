# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.role_attributes import RoleAttributes
    from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
    from datadog_api_client.v2.model.roles_type import RolesType


class Role(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role_attributes import RoleAttributes
        from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
        from datadog_api_client.v2.model.roles_type import RolesType

        return {
            "attributes": (RoleAttributes,),
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

    def __init__(
        self_,
        id: str,
        type: RolesType,
        attributes: Union[RoleAttributes, UnsetType] = unset,
        relationships: Union[RoleResponseRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Role object returned by the API.

        :param attributes: Attributes of the role.
        :type attributes: RoleAttributes, optional

        :param id: The unique identifier of the role.
        :type id: str

        :param relationships: Relationships of the role object returned by the API.
        :type relationships: RoleResponseRelationships, optional

        :param type: Roles type.
        :type type: RolesType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
