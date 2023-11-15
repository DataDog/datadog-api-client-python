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
    from datadog_api_client.v2.model.security_monitoring_rule_types import SecurityMonitoringRuleTypes
    from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity


class SecurityMonitoringNotificationRuleSelectors(ModelNormal):
    validations = {
        "rule_tags": {
            "max_items": 20,
        },
        "signal_tags": {
            "max_items": 20,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_types import SecurityMonitoringRuleTypes
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "attributes": ([str],),
            "implicit_vm_rule_match": (bool,),
            "rule_tags": ([str],),
            "rule_types": ([SecurityMonitoringRuleTypes],),
            "severities": ([SecurityMonitoringRuleSeverity],),
            "signal_tags": ([str],),
        }

    attribute_map = {
        "attributes": "attributes",
        "implicit_vm_rule_match": "implicit_vm_rule_match",
        "rule_tags": "rule_tags",
        "rule_types": "rule_types",
        "severities": "severities",
        "signal_tags": "signal_tags",
    }

    def __init__(
        self_,
        attributes: List[str],
        implicit_vm_rule_match: bool,
        rule_tags: List[str],
        rule_types: List[SecurityMonitoringRuleTypes],
        severities: List[SecurityMonitoringRuleSeverity],
        signal_tags: List[str],
        **kwargs,
    ):
        """
        Selectors describing the notification rule.

        :param attributes: Set of rule and signal tags for which a notification will be triggered.
        :type attributes: [str]

        :param implicit_vm_rule_match: Whether vulnerability_management rules are matched by default when the selector for rule type is empty.
        :type implicit_vm_rule_match: bool

        :param rule_tags: Set of rule tags for which a notification will be triggered.
        :type rule_tags: [str]

        :param rule_types: Set of signal types (rule types) for which a notification will be triggered.
        :type rule_types: [SecurityMonitoringRuleTypes]

        :param severities: Set of signal severities (rule case statuses) for which a notification will be triggered.
        :type severities: [SecurityMonitoringRuleSeverity]

        :param signal_tags: Set of signal tags for which a notification will be triggered.
        :type signal_tags: [str]
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.implicit_vm_rule_match = implicit_vm_rule_match
        self_.rule_tags = rule_tags
        self_.rule_types = rule_types
        self_.severities = severities
        self_.signal_tags = signal_tags
