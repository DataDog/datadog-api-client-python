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
    from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
    from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType


class MonitorNotificationRuleCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
        from datadog_api_client.v2.model.monitor_notification_rule_resource_type import (
            MonitorNotificationRuleResourceType,
        )

        return {
            "attributes": (MonitorNotificationRuleAttributes,),
            "type": (MonitorNotificationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: MonitorNotificationRuleAttributes,
        type: Union[MonitorNotificationRuleResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object to create a monitor notification rule.

        :param attributes: Attributes of the monitor notification rule.
        :type attributes: MonitorNotificationRuleAttributes

        :param type: Monitor notification rule resource type.
        :type type: MonitorNotificationRuleResourceType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
