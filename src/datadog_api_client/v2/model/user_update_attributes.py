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


class UserUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "email": (str,),
            "name": (str,),
            "title": (str, none_type),
        }

    attribute_map = {
        "disabled": "disabled",
        "email": "email",
        "name": "name",
        "title": "title",
    }

    def __init__(
        self_,
        disabled: Union[bool, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the edited user.

        :param disabled: When set to ``true`` , the user is deactivated and can no longer log in.
            When ``false`` , the user is active.
        :type disabled: bool, optional

        :param email: The email address of the user, used for login and notifications.
            Must be a valid email format.
        :type email: str, optional

        :param name: The full display name of the user as shown in the Datadog UI.
            Maximum 55 characters, cannot contain ``<`` or ``>``.
        :type name: str, optional

        :param title: The job title of the user (for example, "Senior Engineer" or "Product Manager").
        :type title: str, none_type, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
