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
    from datadog_api_client.v2.model.governance_notification_settings_update_attributes import (
        GovernanceNotificationSettingsUpdateAttributes,
    )
    from datadog_api_client.v2.model.governance_notification_settings_resource_type import (
        GovernanceNotificationSettingsResourceType,
    )


class GovernanceNotificationSettingsUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_notification_settings_update_attributes import (
            GovernanceNotificationSettingsUpdateAttributes,
        )
        from datadog_api_client.v2.model.governance_notification_settings_resource_type import (
            GovernanceNotificationSettingsResourceType,
        )

        return {
            "attributes": (GovernanceNotificationSettingsUpdateAttributes,),
            "type": (GovernanceNotificationSettingsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: GovernanceNotificationSettingsResourceType,
        attributes: Union[GovernanceNotificationSettingsUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data of a governance notification settings update request.

        :param attributes: The attributes of the governance notification settings that can be updated. Only the attributes present in the request are modified.
        :type attributes: GovernanceNotificationSettingsUpdateAttributes, optional

        :param type: Governance notification settings resource type.
        :type type: GovernanceNotificationSettingsResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
