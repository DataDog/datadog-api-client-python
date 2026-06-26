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
    from datadog_api_client.v2.model.governance_notification_settings_update_data import (
        GovernanceNotificationSettingsUpdateData,
    )


class GovernanceNotificationSettingsUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_notification_settings_update_data import (
            GovernanceNotificationSettingsUpdateData,
        )

        return {
            "data": (GovernanceNotificationSettingsUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GovernanceNotificationSettingsUpdateData, **kwargs):
        """
        A request to update the organization-wide governance notification settings.

        :param data: The data of a governance notification settings update request.
        :type data: GovernanceNotificationSettingsUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
