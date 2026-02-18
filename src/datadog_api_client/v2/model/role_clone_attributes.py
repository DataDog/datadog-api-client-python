# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RoleCloneAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "receives_permissions_from": ([str],),
        }

    attribute_map = {
        "name": "name",
        "receives_permissions_from": "receives_permissions_from",
    }

    def __init__(self_, name: str, receives_permissions_from: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes required to create a new role by cloning an existing one.

        :param name: Name of the new role that is cloned.
        :type name: str

        :param receives_permissions_from: The managed role from which this role automatically inherits new permissions.
            Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role".
            If empty or not specified, the role does not automatically inherit permissions from any managed role.
        :type receives_permissions_from: [str], optional
        """
        if receives_permissions_from is not unset:
            kwargs["receives_permissions_from"] = receives_permissions_from
        super().__init__(kwargs)

        self_.name = name
