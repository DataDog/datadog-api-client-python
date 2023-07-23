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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.user_response_included_item import UserResponseIncludedItem
    from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes
    from datadog_api_client.v2.model.organization import Organization
    from datadog_api_client.v2.model.permission import Permission
    from datadog_api_client.v2.model.role import Role


@dataclass
class UsersResponseJSON:
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


class UsersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user import User
        from datadog_api_client.v2.model.user_response_included_item import UserResponseIncludedItem
        from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes

        return {
            "data": ([User],),
            "included": ([UserResponseIncludedItem],),
            "meta": (ResponseMetaAttributes,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }
    json_api_model = UsersResponseJSON

    def __init__(
        self_,
        data: Union[List[User], UnsetType] = unset,
        included: Union[List[Union[UserResponseIncludedItem, Organization, Permission, Role]], UnsetType] = unset,
        meta: Union[ResponseMetaAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing information about multiple users.

        :param data: Array of returned users.
        :type data: [User], optional

        :param included: Array of objects related to the users.
        :type included: [UserResponseIncludedItem], optional

        :param meta: Object describing meta attributes of response.
        :type meta: ResponseMetaAttributes, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
