# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceNotificationSettingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_notifications_enabled": (bool,),
        }

    attribute_map = {
        "assignment_notifications_enabled": "assignment_notifications_enabled",
    }

    def __init__(self_, assignment_notifications_enabled: bool, **kwargs):
        """
        The attributes of the organization-wide governance notification settings.

        :param assignment_notifications_enabled: Whether notifications are sent to users when detections are assigned to them.
        :type assignment_notifications_enabled: bool
        """
        super().__init__(kwargs)

        self_.assignment_notifications_enabled = assignment_notifications_enabled
