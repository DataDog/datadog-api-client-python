# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GovernanceNotificationSettingsUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_notifications_enabled": (bool,),
        }

    attribute_map = {
        "assignment_notifications_enabled": "assignment_notifications_enabled",
    }

    def __init__(self_, assignment_notifications_enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        The attributes of the governance notification settings that can be updated. Only the attributes present in the request are modified.

        :param assignment_notifications_enabled: Whether notifications are sent to users when detections are assigned to them.
        :type assignment_notifications_enabled: bool, optional
        """
        if assignment_notifications_enabled is not unset:
            kwargs["assignment_notifications_enabled"] = assignment_notifications_enabled
        super().__init__(kwargs)
