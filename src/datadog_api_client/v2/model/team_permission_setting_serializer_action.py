# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class TeamPermissionSettingSerializerAction(StringEnum):
    """
    The identifier for the action

    :param value: Must be one of ["manage_membership", "edit"].
    :type value: str
    """

    allowed_values = {
        "manage_membership",
        "edit",
    }
    MANAGE_MEMBERSHIP: ClassVar["TeamPermissionSettingSerializerAction"]
    EDIT: ClassVar["TeamPermissionSettingSerializerAction"]


TeamPermissionSettingSerializerAction.MANAGE_MEMBERSHIP = TeamPermissionSettingSerializerAction("manage_membership")
TeamPermissionSettingSerializerAction.EDIT = TeamPermissionSettingSerializerAction("edit")
