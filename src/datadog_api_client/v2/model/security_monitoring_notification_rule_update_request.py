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
    from datadog_api_client.v2.model.security_monitoring_notification_rule_update_data import (
        SecurityMonitoringNotificationRuleUpdateData,
    )


class SecurityMonitoringNotificationRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_notification_rule_update_data import (
            SecurityMonitoringNotificationRuleUpdateData,
        )

        return {
            "data": (SecurityMonitoringNotificationRuleUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringNotificationRuleUpdateData, **kwargs):
        """
        Request body for updating a security monitoring notification rule.

        :param data: Data containing the patch for a notification rule.
        :type data: SecurityMonitoringNotificationRuleUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
