# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class SecurityMonitoringTriageUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "icon": (str,),
            "id": (int,),
            "name": (str, none_type),
            "uuid": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "icon": "icon",
        "id": "id",
        "name": "name",
        "uuid": "uuid",
    }
    read_only_vars = {
        "icon",
    }

    def __init__(
        self_,
        uuid: str,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object representing a given user entity.

        :param handle: The handle for this user account.
        :type handle: str, optional

        :param icon: Gravatar icon associated to the user.
        :type icon: str, optional

        :param id: Numerical ID assigned by Datadog to this user account.
        :type id: int, optional

        :param name: The name for this user account.
        :type name: str, none_type, optional

        :param uuid: UUID assigned by Datadog to this user account.
        :type uuid: str
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.uuid = uuid
