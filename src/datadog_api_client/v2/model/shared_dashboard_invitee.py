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
)


class SharedDashboardInvitee(ModelNormal):
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

    def __init__(self_, access_expiration: Union[datetime, none_type], created_at: datetime, email: str, **kwargs):
        """
        Invitee that can access an invite-only shared dashboard.

        :param access_expiration: Time when the invitee's access expires.
        :type access_expiration: datetime, none_type

        :param created_at: Time when the invitee was added.
        :type created_at: datetime

        :param email: Email address of the invitee.
        :type email: str
        """
        super().__init__(kwargs)

        self_.access_expiration = access_expiration
        self_.created_at = created_at
        self_.email = email
