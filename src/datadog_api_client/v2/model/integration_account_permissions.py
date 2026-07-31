# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IntegrationAccountPermissions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "resource_id": (str,),
            "user_can_edit": (bool,),
        }

    attribute_map = {
        "resource_id": "resource_id",
        "user_can_edit": "user_can_edit",
    }
    read_only_vars = {
        "resource_id",
        "user_can_edit",
    }

    def __init__(
        self_, resource_id: Union[str, UnsetType] = unset, user_can_edit: Union[bool, UnsetType] = unset, **kwargs
    ):
        """
        Read-only permission information for the account, derived from its restriction policy.

        :param resource_id: Restriction-policy resource identifier of this account.
        :type resource_id: str, optional

        :param user_can_edit: Whether the requesting user may edit this account.
        :type user_can_edit: bool, optional
        """
        if resource_id is not unset:
            kwargs["resource_id"] = resource_id
        if user_can_edit is not unset:
            kwargs["user_can_edit"] = user_can_edit
        super().__init__(kwargs)
