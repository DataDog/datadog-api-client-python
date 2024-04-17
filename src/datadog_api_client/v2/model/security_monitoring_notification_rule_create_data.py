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
    from datadog_api_client.v2.model.security_monitoring_notification_rule_create_attributes import (
        SecurityMonitoringNotificationRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
        SecurityMonitoringNotificationRuleType,
    )


class SecurityMonitoringNotificationRuleCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_notification_rule_create_attributes import (
            SecurityMonitoringNotificationRuleCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
            SecurityMonitoringNotificationRuleType,
        )

        return {
            "attributes": (SecurityMonitoringNotificationRuleCreateAttributes,),
            "type": (SecurityMonitoringNotificationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringNotificationRuleCreateAttributes,
        type: SecurityMonitoringNotificationRuleType,
        **kwargs,
    ):
        """
        Data containing new notification rule attributes.

        :param attributes: Attributes of a notification rule to be created.
        :type attributes: SecurityMonitoringNotificationRuleCreateAttributes

        :param type: The type of the resource. The value should always be ``notification_rules``.
        :type type: SecurityMonitoringNotificationRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
