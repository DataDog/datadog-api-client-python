# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class UserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "last_login_time": (datetime, none_type),
            "mfa_enabled": (bool,),
            "modified_at": (datetime,),
            "name": (str, none_type),
            "service_account": (bool,),
            "status": (str,),
            "title": (str, none_type),
            "uuid": (str,),
            "verified": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "last_login_time": "last_login_time",
        "mfa_enabled": "mfa_enabled",
        "modified_at": "modified_at",
        "name": "name",
        "service_account": "service_account",
        "status": "status",
        "title": "title",
        "uuid": "uuid",
        "verified": "verified",
    }
    read_only_vars = {
        "last_login_time",
        "mfa_enabled",
        "uuid",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        disabled: Union[bool, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        last_login_time: Union[datetime, none_type, UnsetType] = unset,
        mfa_enabled: Union[bool, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        service_account: Union[bool, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        verified: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of user object returned by the API.

        :param created_at: The ISO 8601 timestamp of when the user account was created.
        :type created_at: datetime, optional

        :param disabled: Whether the user account is deactivated. Disabled users cannot log in.
        :type disabled: bool, optional

        :param email: The email address of the user, used for login and notifications.
        :type email: str, optional

        :param handle: The unique handle (username) of the user, typically matching their email prefix.
        :type handle: str, optional

        :param icon: URL of the user's profile icon, typically a Gravatar URL derived from the email address.
        :type icon: str, optional

        :param last_login_time: The ISO 8601 timestamp of the user's most recent login, or null if the user has never logged in.
        :type last_login_time: datetime, none_type, optional

        :param mfa_enabled: Whether multi-factor authentication (MFA) is enabled for the user's account.
        :type mfa_enabled: bool, optional

        :param modified_at: The ISO 8601 timestamp of when the user account was last modified.
        :type modified_at: datetime, optional

        :param name: The full display name of the user as shown in the Datadog UI.
        :type name: str, none_type, optional

        :param service_account: Whether this is a service account rather than a human user.
            Service accounts are used for programmatic API access.
        :type service_account: bool, optional

        :param status: The current status of the user account (for example, ``Active`` , ``Pending`` , or ``Disabled`` ).
        :type status: str, optional

        :param title: The job title of the user (for example, "Senior Engineer" or "Product Manager").
        :type title: str, none_type, optional

        :param uuid: The globally unique identifier (UUID) of the user.
        :type uuid: str, optional

        :param verified: Whether the user's email address has been verified.
        :type verified: bool, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if last_login_time is not unset:
            kwargs["last_login_time"] = last_login_time
        if mfa_enabled is not unset:
            kwargs["mfa_enabled"] = mfa_enabled
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if service_account is not unset:
            kwargs["service_account"] = service_account
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if uuid is not unset:
            kwargs["uuid"] = uuid
        if verified is not unset:
            kwargs["verified"] = verified
        super().__init__(kwargs)
