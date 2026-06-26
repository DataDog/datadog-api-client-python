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
    from datadog_api_client.v2.model.governance_notification_settings_attributes import (
        GovernanceNotificationSettingsAttributes,
    )
    from datadog_api_client.v2.model.governance_notification_settings_resource_type import (
        GovernanceNotificationSettingsResourceType,
    )


class GovernanceNotificationSettingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_notification_settings_attributes import (
            GovernanceNotificationSettingsAttributes,
        )
        from datadog_api_client.v2.model.governance_notification_settings_resource_type import (
            GovernanceNotificationSettingsResourceType,
        )

        return {
            "attributes": (GovernanceNotificationSettingsAttributes,),
            "id": (str,),
            "type": (GovernanceNotificationSettingsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GovernanceNotificationSettingsAttributes,
        id: str,
        type: GovernanceNotificationSettingsResourceType,
        **kwargs,
    ):
        """
        A governance notification settings resource.

        :param attributes: The attributes of the organization-wide governance notification settings.
        :type attributes: GovernanceNotificationSettingsAttributes

        :param id: The unique identifier of the organization the notification settings apply to.
        :type id: str

        :param type: Governance notification settings resource type.
        :type type: GovernanceNotificationSettingsResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
