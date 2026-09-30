# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class RoleUpdateAttributes(ModelNormal):
    validations = {
        "user_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "default_permissions_opt_out": (bool,),
            "modified_at": (datetime,),
            "name": (str,),
            "receives_permissions_from": ([str],),
            "user_count": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "default_permissions_opt_out": "default_permissions_opt_out",
        "modified_at": "modified_at",
        "name": "name",
        "receives_permissions_from": "receives_permissions_from",
        "user_count": "user_count",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        default_permissions_opt_out: Union[bool, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        receives_permissions_from: Union[List[str], UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the role.

        :param created_at: Creation time of the role.
        :type created_at: datetime, optional

        :param default_permissions_opt_out: Whether to exclude restricted default permissions from this role.
            Restricted default permissions are automatically assigned to every role by default. Set this field to ``true`` to exclude them.
            Some of these permissions can only be excluded after Minimal Access Roles is enabled for the organization.
        :type default_permissions_opt_out: bool, optional

        :param modified_at: Time of last role modification.
        :type modified_at: datetime, optional

        :param name: Name of the role.
        :type name: str, optional

        :param receives_permissions_from: The managed role from which this role automatically inherits new permissions.
            Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role".
            If empty or not specified, the role does not automatically inherit permissions from any managed role.
        :type receives_permissions_from: [str], optional

        :param user_count: The user count.
        :type user_count: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if default_permissions_opt_out is not unset:
            kwargs["default_permissions_opt_out"] = default_permissions_opt_out
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if receives_permissions_from is not unset:
            kwargs["receives_permissions_from"] = receives_permissions_from
        if user_count is not unset:
            kwargs["user_count"] = user_count
        super().__init__(kwargs)
