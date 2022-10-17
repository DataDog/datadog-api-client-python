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
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.user_attributes import UserAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships
    from datadog_api_client.v2.model.users_type import UsersType


@dataclass
class UserJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    disabled: Union[bool, UnsetType] = unset
    email: Union[str, UnsetType] = unset
    handle: Union[str, UnsetType] = unset
    icon: Union[str, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, none_type, UnsetType] = unset
    service_account: Union[bool, UnsetType] = unset
    status: Union[str, UnsetType] = unset
    title: Union[str, none_type, UnsetType] = unset
    verified: Union[bool, UnsetType] = unset
    org: Union[str, UnsetType] = unset
    other_orgs: Union[List[str], UnsetType] = unset
    other_users: Union[List[str], UnsetType] = unset
    roles: Union[List[str], UnsetType] = unset


class User(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships
        from datadog_api_client.v2.model.users_type import UsersType

        return {
            "attributes": (UserAttributes,),
            "id": (str,),
            "relationships": (UserResponseRelationships,),
            "type": (UsersType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }
    json_api_model = UserJSON

    def __init__(
        self_,
        attributes: Union[UserAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[UserResponseRelationships, UnsetType] = unset,
        type: Union[UsersType, UnsetType] = unset,
        **kwargs,
    ):
        """
        User object returned by the API.

        :param attributes: Attributes of user object returned by the API.
        :type attributes: UserAttributes, optional

        :param id: ID of the user.
        :type id: str, optional

        :param relationships: Relationships of the user object returned by the API.
        :type relationships: UserResponseRelationships, optional

        :param type: Users resource type.
        :type type: UsersType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
