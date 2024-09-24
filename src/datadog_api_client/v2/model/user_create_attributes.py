# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class UserCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "service_account": (bool,),
            "title": (str,),
            "verified": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "modified_at": "modified_at",
        "name": "name",
        "service_account": "service_account",
        "title": "title",
        "verified": "verified",
    }

    def __init__(
        self_,
        email: str,
        created_at: Union[datetime, UnsetType] = unset,
        disabled: Union[bool, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        service_account: Union[bool, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        verified: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the created user.

        :param created_at: The ``UserCreateAttributes`` ``created_at``.
        :type created_at: datetime, optional

        :param disabled: The ``UserCreateAttributes`` ``disabled``.
        :type disabled: bool, optional

        :param email: The email of the user.
        :type email: str

        :param handle: The ``UserCreateAttributes`` ``handle``.
        :type handle: str, optional

        :param modified_at: The ``UserCreateAttributes`` ``modified_at``.
        :type modified_at: datetime, optional

        :param name: The name of the user.
        :type name: str, optional

        :param service_account: The ``UserCreateAttributes`` ``service_account``.
        :type service_account: bool, optional

        :param title: The title of the user.
        :type title: str, optional

        :param verified: The ``UserCreateAttributes`` ``verified``.
        :type verified: bool, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if handle is not unset:
            kwargs["handle"] = handle
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if service_account is not unset:
            kwargs["service_account"] = service_account
        if title is not unset:
            kwargs["title"] = title
        if verified is not unset:
            kwargs["verified"] = verified
        super().__init__(kwargs)

        self_.email = email
