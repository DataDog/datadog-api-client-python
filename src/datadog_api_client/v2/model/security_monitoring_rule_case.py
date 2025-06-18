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
    from datadog_api_client.v2.model.security_monitoring_rule_case_action import SecurityMonitoringRuleCaseAction
    from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity


class SecurityMonitoringRuleCase(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case_action import SecurityMonitoringRuleCaseAction
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "actions": ([SecurityMonitoringRuleCaseAction],),
            "condition": (str,),
            "custom_status": (SecurityMonitoringRuleSeverity,),
            "name": (str,),
            "notifications": ([str],),
            "status": (SecurityMonitoringRuleSeverity,),
        }

    attribute_map = {
        "actions": "actions",
        "condition": "condition",
        "custom_status": "customStatus",
        "name": "name",
        "notifications": "notifications",
        "status": "status",
    }

    def __init__(
        self_,
        actions: Union[List[SecurityMonitoringRuleCaseAction], UnsetType] = unset,
        condition: Union[str, UnsetType] = unset,
        custom_status: Union[SecurityMonitoringRuleSeverity, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        notifications: Union[List[str], UnsetType] = unset,
        status: Union[SecurityMonitoringRuleSeverity, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case when signal is generated.

        :param actions: Action to perform for each rule case.
        :type actions: [SecurityMonitoringRuleCaseAction], optional

        :param condition: A rule case contains logical operations ( ``>`` , ``>=`` , ``&&`` , ``||`` ) to determine if a signal should be generated
            based on the event counts in the previously defined queries.
        :type condition: str, optional

        :param custom_status: Severity of the Security Signal.
        :type custom_status: SecurityMonitoringRuleSeverity, optional

        :param name: Name of the case.
        :type name: str, optional

        :param notifications: Notification targets for each rule case.
        :type notifications: [str], optional

        :param status: Severity of the Security Signal.
        :type status: SecurityMonitoringRuleSeverity, optional
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if condition is not unset:
            kwargs["condition"] = condition
        if custom_status is not unset:
            kwargs["custom_status"] = custom_status
        if name is not unset:
            kwargs["name"] = name
        if notifications is not unset:
            kwargs["notifications"] = notifications
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
