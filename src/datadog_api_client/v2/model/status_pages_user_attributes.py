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


class StatusPagesUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param email:
        :type email: str, optional

        :param handle:
        :type handle: str, optional

        :param icon:
        :type icon: str, optional

        :param name:
        :type name: str, optional

        :param uuid:
        :type uuid: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)
