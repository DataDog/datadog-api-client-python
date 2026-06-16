# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationRulePreviewNotificationStatus(ModelSimple):
    """
    The notification status for the given rule type. `SUCCESS` means a matching event was found and the notification was sent successfully. `DEFAULT` means no matching event was found and a default placeholder notification was sent instead. `ERROR` means an error occurred while sending the notification.

    :param value: Must be one of ["SUCCESS", "DEFAULT", "ERROR"].
    :type value: str
    """

    allowed_values = {
        "SUCCESS",
        "DEFAULT",
        "ERROR",
    }
    SUCCESS: ClassVar["NotificationRulePreviewNotificationStatus"]
    DEFAULT: ClassVar["NotificationRulePreviewNotificationStatus"]
    ERROR: ClassVar["NotificationRulePreviewNotificationStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationRulePreviewNotificationStatus.SUCCESS = NotificationRulePreviewNotificationStatus("SUCCESS")
NotificationRulePreviewNotificationStatus.DEFAULT = NotificationRulePreviewNotificationStatus("DEFAULT")
NotificationRulePreviewNotificationStatus.ERROR = NotificationRulePreviewNotificationStatus("ERROR")
