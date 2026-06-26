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
    from datadog_api_client.v2.model.control_notification_settings_attributes import (
        ControlNotificationSettingsAttributes,
    )
    from datadog_api_client.v2.model.control_notification_settings_resource_type import (
        ControlNotificationSettingsResourceType,
    )


class ControlNotificationSettingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.control_notification_settings_attributes import (
            ControlNotificationSettingsAttributes,
        )
        from datadog_api_client.v2.model.control_notification_settings_resource_type import (
            ControlNotificationSettingsResourceType,
        )

        return {
            "attributes": (ControlNotificationSettingsAttributes,),
            "id": (str,),
            "type": (ControlNotificationSettingsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ControlNotificationSettingsAttributes,
        id: str,
        type: ControlNotificationSettingsResourceType,
        **kwargs,
    ):
        """
        A control notification settings resource.

        :param attributes: The attributes of a governance control's notification settings.
        :type attributes: ControlNotificationSettingsAttributes

        :param id: The detection type the notification settings apply to.
        :type id: str

        :param type: Control notification settings resource type.
        :type type: ControlNotificationSettingsResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
