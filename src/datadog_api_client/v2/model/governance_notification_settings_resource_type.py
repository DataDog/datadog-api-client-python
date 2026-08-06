# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceNotificationSettingsResourceType(ModelSimple):
    """
    Governance notification settings resource type.

    :param value: If omitted defaults to "governance_notification_settings". Must be one of ["governance_notification_settings"].
    :type value: str
    """

    allowed_values = {
        "governance_notification_settings",
    }
    GOVERNANCE_NOTIFICATION_SETTINGS: ClassVar["GovernanceNotificationSettingsResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceNotificationSettingsResourceType.GOVERNANCE_NOTIFICATION_SETTINGS = (
    GovernanceNotificationSettingsResourceType("governance_notification_settings")
)
