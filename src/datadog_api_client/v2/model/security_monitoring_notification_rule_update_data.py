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
    from datadog_api_client.v2.model.security_monitoring_notification_rule_update_attributes import (
        SecurityMonitoringNotificationRuleUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
        SecurityMonitoringNotificationRuleType,
    )


class SecurityMonitoringNotificationRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_notification_rule_update_attributes import (
            SecurityMonitoringNotificationRuleUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
            SecurityMonitoringNotificationRuleType,
        )

        return {
            "attributes": (SecurityMonitoringNotificationRuleUpdateAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringNotificationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringNotificationRuleUpdateAttributes,
        type: SecurityMonitoringNotificationRuleType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data containing the patch for a notification rule.

        :param attributes: Attributes of a notification rule to be updated.
        :type attributes: SecurityMonitoringNotificationRuleUpdateAttributes

        :param id: The unique ID of the notification rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``notification_rules``.
        :type type: SecurityMonitoringNotificationRuleType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
