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
    from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
    from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
        CloudConfigurationRuleComplianceSignalOptions,
    )
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery
    from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
    from datadog_api_client.v2.model.security_monitoring_third_party_rule_case import (
        SecurityMonitoringThirdPartyRuleCase,
    )
    from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
    from datadog_api_client.v2.model.security_monitoring_signal_rule_query import SecurityMonitoringSignalRuleQuery


class SecurityMonitoringRuleUpdatePayload(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
        from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
            CloudConfigurationRuleComplianceSignalOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery
        from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
        from datadog_api_client.v2.model.security_monitoring_third_party_rule_case import (
            SecurityMonitoringThirdPartyRuleCase,
        )

        return {
            "cases": ([SecurityMonitoringRuleCase],),
            "compliance_signal_options": (CloudConfigurationRuleComplianceSignalOptions,),
            "custom_message": (str,),
            "custom_name": (str,),
            "filters": ([SecurityMonitoringFilter],),
            "group_signals_by": ([str],),
            "has_extended_title": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringRuleQuery],),
            "reference_tables": ([SecurityMonitoringReferenceTable],),
            "tags": ([str],),
            "third_party_cases": ([SecurityMonitoringThirdPartyRuleCase],),
            "version": (int,),
        }

    attribute_map = {
        "cases": "cases",
        "compliance_signal_options": "complianceSignalOptions",
        "custom_message": "customMessage",
        "custom_name": "customName",
        "filters": "filters",
        "group_signals_by": "groupSignalsBy",
        "has_extended_title": "hasExtendedTitle",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "reference_tables": "referenceTables",
        "tags": "tags",
        "third_party_cases": "thirdPartyCases",
        "version": "version",
    }

    def __init__(
        self_,
        cases: Union[List[SecurityMonitoringRuleCase], UnsetType] = unset,
        compliance_signal_options: Union[CloudConfigurationRuleComplianceSignalOptions, UnsetType] = unset,
        custom_message: Union[str, UnsetType] = unset,
        custom_name: Union[str, UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        group_signals_by: Union[List[str], UnsetType] = unset,
        has_extended_title: Union[bool, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        options: Union[SecurityMonitoringRuleOptions, UnsetType] = unset,
        queries: Union[
            List[
                Union[
                    SecurityMonitoringRuleQuery, SecurityMonitoringStandardRuleQuery, SecurityMonitoringSignalRuleQuery
                ]
            ],
            UnsetType,
        ] = unset,
        reference_tables: Union[List[SecurityMonitoringReferenceTable], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        third_party_cases: Union[List[SecurityMonitoringThirdPartyRuleCase], UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Update an existing rule.

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCase], optional

        :param compliance_signal_options: How to generate compliance signals. Useful for cloud_configuration rules only.
        :type compliance_signal_options: CloudConfigurationRuleComplianceSignalOptions, optional

        :param custom_message: Custom/Overridden Message for generated signals (used in case of Default rule update).
        :type custom_message: str, optional

        :param custom_name: Custom/Overridden name (used in case of Default rule update).
        :type custom_name: str, optional

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param group_signals_by: Additional grouping to perform on top of the existing groups in the query section. Must be a subset of the existing groups.
        :type group_signals_by: [str], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool, optional

        :param message: Message for generated signals.
        :type message: str, optional

        :param name: Name of the rule.
        :type name: str, optional

        :param options: Options.
        :type options: SecurityMonitoringRuleOptions, optional

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringRuleQuery], optional

        :param reference_tables: Reference tables for the rule.
        :type reference_tables: [SecurityMonitoringReferenceTable], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param third_party_cases: Cases for generating signals from third-party rules. Only available for third-party rules.
        :type third_party_cases: [SecurityMonitoringThirdPartyRuleCase], optional

        :param version: The version of the rule being updated.
        :type version: int, optional
        """
        if cases is not unset:
            kwargs["cases"] = cases
        if compliance_signal_options is not unset:
            kwargs["compliance_signal_options"] = compliance_signal_options
        if custom_message is not unset:
            kwargs["custom_message"] = custom_message
        if custom_name is not unset:
            kwargs["custom_name"] = custom_name
        if filters is not unset:
            kwargs["filters"] = filters
        if group_signals_by is not unset:
            kwargs["group_signals_by"] = group_signals_by
        if has_extended_title is not unset:
            kwargs["has_extended_title"] = has_extended_title
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if message is not unset:
            kwargs["message"] = message
        if name is not unset:
            kwargs["name"] = name
        if options is not unset:
            kwargs["options"] = options
        if queries is not unset:
            kwargs["queries"] = queries
        if reference_tables is not unset:
            kwargs["reference_tables"] = reference_tables
        if tags is not unset:
            kwargs["tags"] = tags
        if third_party_cases is not unset:
            kwargs["third_party_cases"] = third_party_cases
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
