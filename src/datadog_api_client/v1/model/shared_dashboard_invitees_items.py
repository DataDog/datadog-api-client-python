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


class SharedDashboardInviteesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "access_expiration": (datetime, none_type),
            "created_at": (datetime,),
            "email": (str,),
        }

    attribute_map = {
        "access_expiration": "access_expiration",
        "created_at": "created_at",
        "email": "email",
    }
    read_only_vars = {
        "created_at",
    }

    def __init__(
        self_,
        email: str,
        access_expiration: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The allowlisted invitees for an INVITE-only shared dashboard.

        :param access_expiration: Time of the invitee expiration. Null means the invite will not expire.
        :type access_expiration: datetime, none_type, optional

        :param created_at: Time that the invitee was created.
        :type created_at: datetime, optional

        :param email: Email of the invitee.
        :type email: str
        """
        if access_expiration is not unset:
            kwargs["access_expiration"] = access_expiration
        if created_at is not unset:
            kwargs["created_at"] = created_at
        super().__init__(kwargs)

        self_.email = email
