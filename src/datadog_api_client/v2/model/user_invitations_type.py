# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class UserInvitationsType(StringEnum):
    """
    User invitations type.

    :param value: If omitted defaults to "user_invitations". Must be one of ["user_invitations"].
    :type value: str
    """

    allowed_values = {
        "user_invitations",
    }
    USER_INVITATIONS: ClassVar["UserInvitationsType"]


UserInvitationsType.USER_INVITATIONS = UserInvitationsType("user_invitations")
