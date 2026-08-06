# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_notification_settings_data import GovernanceNotificationSettingsData


class GovernanceNotificationSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_notification_settings_data import GovernanceNotificationSettingsData

        return {
            "data": (GovernanceNotificationSettingsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GovernanceNotificationSettingsData, **kwargs):
        """
        The organization-wide governance notification settings.

        :param data: A governance notification settings resource.
        :type data: GovernanceNotificationSettingsData
        """
        super().__init__(kwargs)

        self_.data = data
