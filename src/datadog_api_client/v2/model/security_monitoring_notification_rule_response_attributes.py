# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_creator import SecurityMonitoringCreator
    from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
        SecurityMonitoringNotificationRuleSelectors,
    )
    from datadog_api_client.v2.model.security_monitoring_updater import SecurityMonitoringUpdater


class SecurityMonitoringNotificationRuleResponseAttributes(ModelNormal):
    validations = {
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
        from datadog_api_client.v2.model.security_monitoring_creator import SecurityMonitoringCreator
        from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
            SecurityMonitoringNotificationRuleSelectors,
        )
        from datadog_api_client.v2.model.security_monitoring_updater import SecurityMonitoringUpdater

        return {
            "creation_date": (int,),
            "creator": (SecurityMonitoringCreator,),
            "enabled": (bool,),
            "name": (str,),
            "selectors": (SecurityMonitoringNotificationRuleSelectors,),
            "targets": ([str],),
            "update_date": (int,),
            "updater": (SecurityMonitoringUpdater,),
            "version": (int,),
        }

    attribute_map = {
        "creation_date": "creation_date",
        "creator": "creator",
        "enabled": "enabled",
        "name": "name",
        "selectors": "selectors",
        "targets": "targets",
        "update_date": "update_date",
        "updater": "updater",
        "version": "version",
    }

    def __init__(
        self_,
        creation_date: Union[int, UnsetType] = unset,
        creator: Union[SecurityMonitoringCreator, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        selectors: Union[SecurityMonitoringNotificationRuleSelectors, UnsetType] = unset,
        targets: Union[List[str], UnsetType] = unset,
        update_date: Union[int, UnsetType] = unset,
        updater: Union[SecurityMonitoringUpdater, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the notification rule.

        :param creation_date: Timestamp of creation of the notification rule in milliseconds.
        :type creation_date: int, optional

        :param creator: The author of the notification rule.
        :type creator: SecurityMonitoringCreator, optional

        :param enabled: Whether the notification rule is enabled.
        :type enabled: bool, optional

        :param name: The name of the notification rule.
        :type name: str, optional

        :param selectors: Selectors describing the notification rule.
        :type selectors: SecurityMonitoringNotificationRuleSelectors, optional

        :param targets: Set of targets to notify.
        :type targets: [str], optional

        :param update_date: Timestamp of last modification of the notification rule in milliseconds.
        :type update_date: int, optional

        :param updater: The editor of the notification rule.
        :type updater: SecurityMonitoringUpdater, optional

        :param version: The version of the rule being updated.
        :type version: int, optional
        """
        if creation_date is not unset:
            kwargs["creation_date"] = creation_date
        if creator is not unset:
            kwargs["creator"] = creator
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        if selectors is not unset:
            kwargs["selectors"] = selectors
        if targets is not unset:
            kwargs["targets"] = targets
        if update_date is not unset:
            kwargs["update_date"] = update_date
        if updater is not unset:
            kwargs["updater"] = updater
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
