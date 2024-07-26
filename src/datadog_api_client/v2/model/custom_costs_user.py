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


class CustomCostsUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "icon": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "icon": "icon",
        "name": "name",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata of the user that has uploaded the Custom Costs file.

        :param email: The name of the Custom Costs file.
        :type email: str, optional

        :param icon: The name of the Custom Costs file.
        :type icon: str, optional

        :param name: Name of the user.
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
