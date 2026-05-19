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


class DashboardUsageUser(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "id": (str,),
            "is_disabled": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "id": "id",
        "is_disabled": "is_disabled",
        "name": "name",
    }

    def __init__(
        self_,
        handle: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_disabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A user referenced from a dashboard usage record (author or viewer).

        :param handle: Datadog handle (login) of the user.
        :type handle: str, optional

        :param id: The user ID.
        :type id: str, optional

        :param is_disabled: Whether the user account is disabled.
        :type is_disabled: bool, optional

        :param name: Display name of the user.
        :type name: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if id is not unset:
            kwargs["id"] = id
        if is_disabled is not unset:
            kwargs["is_disabled"] = is_disabled
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
