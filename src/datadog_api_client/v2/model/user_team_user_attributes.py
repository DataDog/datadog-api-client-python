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


class UserTeamUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "name": (str, none_type),
            "service_account": (bool,),
        }

    attribute_map = {
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "name": "name",
        "service_account": "service_account",
    }

    def __init__(
        self_,
        disabled: Union[bool, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        service_account: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UserTeamUserAttributes`` object.

        :param disabled: The ``UserTeamUserAttributes`` ``disabled``.
        :type disabled: bool, optional

        :param email: The ``UserTeamUserAttributes`` ``email``.
        :type email: str, optional

        :param handle: The ``UserTeamUserAttributes`` ``handle``.
        :type handle: str, optional

        :param icon: The ``UserTeamUserAttributes`` ``icon``.
        :type icon: str, optional

        :param name: The ``UserTeamUserAttributes`` ``name``.
        :type name: str, none_type, optional

        :param service_account: The ``UserTeamUserAttributes`` ``service_account``.
        :type service_account: bool, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        if service_account is not unset:
            kwargs["service_account"] = service_account
        super().__init__(kwargs)
