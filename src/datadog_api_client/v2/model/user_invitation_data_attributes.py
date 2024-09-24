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


class UserInvitationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "expires_at": (datetime,),
            "invite_type": (str,),
            "login_method": (str, none_type),
            "uuid": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "expires_at": "expires_at",
        "invite_type": "invite_type",
        "login_method": "login_method",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        expires_at: Union[datetime, UnsetType] = unset,
        invite_type: Union[str, UnsetType] = unset,
        login_method: Union[str, none_type, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a user invitation.

        :param created_at: Creation time of the user invitation.
        :type created_at: datetime, optional

        :param expires_at: Time of invitation expiration.
        :type expires_at: datetime, optional

        :param invite_type: Type of invitation.
        :type invite_type: str, optional

        :param login_method: The ``UserInvitationDataAttributes`` ``login_method``.
        :type login_method: str, none_type, optional

        :param uuid: UUID of the user invitation.
        :type uuid: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if expires_at is not unset:
            kwargs["expires_at"] = expires_at
        if invite_type is not unset:
            kwargs["invite_type"] = invite_type
        if login_method is not unset:
            kwargs["login_method"] = login_method
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)
