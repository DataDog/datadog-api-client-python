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
    from datadog_api_client.v2.model.security_monitoring_notification_rule_response_attributes import (
        SecurityMonitoringNotificationRuleResponseAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
        SecurityMonitoringNotificationRuleType,
    )


class SecurityMonitoringNotificationRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_notification_rule_response_attributes import (
            SecurityMonitoringNotificationRuleResponseAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
            SecurityMonitoringNotificationRuleType,
        )

        return {
            "attributes": (SecurityMonitoringNotificationRuleResponseAttributes,),
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
        attributes: Union[SecurityMonitoringNotificationRuleResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityMonitoringNotificationRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data containing notification rule attributes.

        :param attributes: Attributes of the notification rule.
        :type attributes: SecurityMonitoringNotificationRuleResponseAttributes, optional

        :param id: The unique ID of the notification rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``notification_rules``.
        :type type: SecurityMonitoringNotificationRuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
