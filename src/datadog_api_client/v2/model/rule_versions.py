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
    from datadog_api_client.v2.model.rule_version_update import RuleVersionUpdate
    from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse
    from datadog_api_client.v2.model.security_monitoring_standard_rule_response import (
        SecurityMonitoringStandardRuleResponse,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_rule_response import (
        SecurityMonitoringSignalRuleResponse,
    )


class RuleVersions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_version_update import RuleVersionUpdate
        from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse

        return {
            "changes": ([RuleVersionUpdate],),
            "rule": (SecurityMonitoringRuleResponse,),
        }

    attribute_map = {
        "changes": "changes",
        "rule": "rule",
    }

    def __init__(
        self_,
        changes: Union[List[RuleVersionUpdate], UnsetType] = unset,
        rule: Union[
            SecurityMonitoringRuleResponse,
            SecurityMonitoringStandardRuleResponse,
            SecurityMonitoringSignalRuleResponse,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        A rule version with a list of updates.

        :param changes: A list of changes.
        :type changes: [RuleVersionUpdate], optional

        :param rule: Create a new rule.
        :type rule: SecurityMonitoringRuleResponse, optional
        """
        if changes is not unset:
            kwargs["changes"] = changes
        if rule is not unset:
            kwargs["rule"] = rule
        super().__init__(kwargs)
