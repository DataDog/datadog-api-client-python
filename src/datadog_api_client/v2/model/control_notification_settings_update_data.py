# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.control_notification_settings_update_attributes import (
        ControlNotificationSettingsUpdateAttributes,
    )
    from datadog_api_client.v2.model.control_notification_settings_resource_type import (
        ControlNotificationSettingsResourceType,
    )


class ControlNotificationSettingsUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.control_notification_settings_update_attributes import (
            ControlNotificationSettingsUpdateAttributes,
        )
        from datadog_api_client.v2.model.control_notification_settings_resource_type import (
            ControlNotificationSettingsResourceType,
        )

        return {
            "attributes": (ControlNotificationSettingsUpdateAttributes,),
            "type": (ControlNotificationSettingsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: ControlNotificationSettingsResourceType,
        attributes: Union[ControlNotificationSettingsUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data of a control notification settings update request.

        :param attributes: The attributes of a governance control's notification settings that can be updated.
        :type attributes: ControlNotificationSettingsUpdateAttributes, optional

        :param type: Control notification settings resource type.
        :type type: ControlNotificationSettingsResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
