# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
        SecurityMonitoringNotificationRuleSelectors,
    )


class SecurityMonitoringNotificationRuleUpdateAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 500,
            "min_length": 1,
        },
        "targets": {
            "max_items": 20,
            "min_items": 1,
        },
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
            SecurityMonitoringNotificationRuleSelectors,
        )

        return {
            "enabled": (bool,),
            "name": (str,),
            "selectors": (SecurityMonitoringNotificationRuleSelectors,),
            "targets": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
        "selectors": "selectors",
        "targets": "targets",
        "version": "version",
    }

    def __init__(
        self_,
        enabled: bool,
        name: str,
        selectors: SecurityMonitoringNotificationRuleSelectors,
        targets: List[str],
        version: int,
        **kwargs,
    ):
        """
        Attributes of a notification rule to be updated.

        :param enabled: Whether the notification rule is enabled.
        :type enabled: bool

        :param name: The name of the notification rule.
        :type name: str

        :param selectors: Selectors describing the notification rule.
        :type selectors: SecurityMonitoringNotificationRuleSelectors

        :param targets: Set of targets to notify.
        :type targets: [str]

        :param version: The version of the rule being updated.
        :type version: int
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.name = name
        self_.selectors = selectors
        self_.targets = targets
        self_.version = version
