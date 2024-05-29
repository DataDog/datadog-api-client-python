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
    from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
    from datadog_api_client.v2.model.security_monitoring_rule_query_payload import SecurityMonitoringRuleQueryPayload
    from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
        SecurityMonitoringStandardRuleCreatePayload,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_rule_create_payload import (
        SecurityMonitoringSignalRuleCreatePayload,
    )
    from datadog_api_client.v2.model.cloud_configuration_rule_create_payload import CloudConfigurationRuleCreatePayload


class SecurityMonitoringRuleTestRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_create_payload import (
            SecurityMonitoringRuleCreatePayload,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_query_payload import (
            SecurityMonitoringRuleQueryPayload,
        )

        return {
            "rule": (SecurityMonitoringRuleCreatePayload,),
            "rule_query_payloads": ([SecurityMonitoringRuleQueryPayload],),
        }

    attribute_map = {
        "rule": "rule",
        "rule_query_payloads": "ruleQueryPayloads",
    }

    def __init__(
        self_,
        rule: Union[
            SecurityMonitoringRuleCreatePayload,
            SecurityMonitoringStandardRuleCreatePayload,
            SecurityMonitoringSignalRuleCreatePayload,
            CloudConfigurationRuleCreatePayload,
            UnsetType,
        ] = unset,
        rule_query_payloads: Union[List[SecurityMonitoringRuleQueryPayload], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test the rule queries of a rule.

        :param rule: Create a new rule.
        :type rule: SecurityMonitoringRuleCreatePayload, optional

        :param rule_query_payloads: Data payloads used to test rules query with the expected result.
        :type rule_query_payloads: [SecurityMonitoringRuleQueryPayload], optional
        """
        if rule is not unset:
            kwargs["rule"] = rule
        if rule_query_payloads is not unset:
            kwargs["rule_query_payloads"] = rule_query_payloads
        super().__init__(kwargs)
