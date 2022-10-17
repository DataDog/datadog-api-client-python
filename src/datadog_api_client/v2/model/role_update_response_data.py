# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
    from datadog_api_client.v2.model.roles_type import RolesType


@dataclass
class RoleUpdateResponseDataJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    permissions: Union[List[str], UnsetType] = unset


class RoleUpdateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
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
    json_api_model = RoleUpdateResponseDataJSON

    def __init__(
        self_,
        type: RolesType,
        attributes: Union[RoleUpdateAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[RoleResponseRelationships, UnsetType] = unset,
        **kwargs,
    ):
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
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
