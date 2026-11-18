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


class ProductAnalyticsMonitorCreator(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "id": (int,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "id": "id",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The user who created the monitor.

        :param email: Email of the user.
        :type email: str, optional

        :param handle: Handle of the user.
        :type handle: str, optional

        :param id: Numeric ID of the user.
        :type id: int, optional

        :param name: Name of the user.
        :type name: str, optional

        :param uuid: UUID of the user.
        :type uuid: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)
