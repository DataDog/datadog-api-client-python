# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.calculated_field import CalculatedField
    from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
    from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
    from datadog_api_client.v2.model.security_monitoring_scheduling_options import SecurityMonitoringSchedulingOptions
    from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
        SecurityMonitoringThirdPartyRuleCaseCreate,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_type_test import SecurityMonitoringRuleTypeTest


class SecurityMonitoringStandardRuleTestPayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.calculated_field import CalculatedField
        from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_standard_rule_query import (
            SecurityMonitoringStandardRuleQuery,
        )
        from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
        from datadog_api_client.v2.model.security_monitoring_scheduling_options import (
            SecurityMonitoringSchedulingOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
            SecurityMonitoringThirdPartyRuleCaseCreate,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_type_test import SecurityMonitoringRuleTypeTest

        return {
            "calculated_fields": ([CalculatedField],),
            "cases": ([SecurityMonitoringRuleCaseCreate],),
            "filters": ([SecurityMonitoringFilter],),
            "group_signals_by": ([str],),
            "has_extended_title": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringStandardRuleQuery],),
            "reference_tables": ([SecurityMonitoringReferenceTable],),
            "scheduling_options": (SecurityMonitoringSchedulingOptions,),
            "tags": ([str],),
            "third_party_cases": ([SecurityMonitoringThirdPartyRuleCaseCreate],),
            "type": (SecurityMonitoringRuleTypeTest,),
        }

    attribute_map = {
        "calculated_fields": "calculatedFields",
        "cases": "cases",
        "filters": "filters",
        "group_signals_by": "groupSignalsBy",
        "has_extended_title": "hasExtendedTitle",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "reference_tables": "referenceTables",
        "scheduling_options": "schedulingOptions",
        "tags": "tags",
        "third_party_cases": "thirdPartyCases",
        "type": "type",
    }

    def __init__(
        self_,
        cases: List[SecurityMonitoringRuleCaseCreate],
        is_enabled: bool,
        message: str,
        name: str,
        options: SecurityMonitoringRuleOptions,
        queries: List[SecurityMonitoringStandardRuleQuery],
        calculated_fields: Union[List[CalculatedField], UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        group_signals_by: Union[List[str], UnsetType] = unset,
        has_extended_title: Union[bool, UnsetType] = unset,
        reference_tables: Union[List[SecurityMonitoringReferenceTable], UnsetType] = unset,
        scheduling_options: Union[SecurityMonitoringSchedulingOptions, none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        third_party_cases: Union[List[SecurityMonitoringThirdPartyRuleCaseCreate], UnsetType] = unset,
        type: Union[SecurityMonitoringRuleTypeTest, UnsetType] = unset,
        **kwargs,
    ):
        """
        The payload of a rule to test

        :param calculated_fields: Calculated fields. Only allowed for scheduled rules - in other words, when schedulingOptions is also defined.
        :type calculated_fields: [CalculatedField], optional

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCaseCreate]

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param group_signals_by: Additional grouping to perform on top of the existing groups in the query section. Must be a subset of the existing groups.
        :type group_signals_by: [str], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool

        :param message: Message for generated signals.
        :type message: str

        :param name: The name of the rule.
        :type name: str

        :param options: Options.
        :type options: SecurityMonitoringRuleOptions

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringStandardRuleQuery]

        :param reference_tables: Reference tables for the rule.
        :type reference_tables: [SecurityMonitoringReferenceTable], optional

        :param scheduling_options: Options for scheduled rules. When this field is present, the rule runs based on the schedule. When absent, it runs real-time on ingested logs.
        :type scheduling_options: SecurityMonitoringSchedulingOptions, none_type, optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param third_party_cases: Cases for generating signals from third-party rules. Only available for third-party rules.
        :type third_party_cases: [SecurityMonitoringThirdPartyRuleCaseCreate], optional

        :param type: The rule type.
        :type type: SecurityMonitoringRuleTypeTest, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if filters is not unset:
            kwargs["filters"] = filters
        if group_signals_by is not unset:
            kwargs["group_signals_by"] = group_signals_by
        if has_extended_title is not unset:
            kwargs["has_extended_title"] = has_extended_title
        if reference_tables is not unset:
            kwargs["reference_tables"] = reference_tables
        if scheduling_options is not unset:
            kwargs["scheduling_options"] = scheduling_options
        if tags is not unset:
            kwargs["tags"] = tags
        if third_party_cases is not unset:
            kwargs["third_party_cases"] = third_party_cases
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.cases = cases
        self_.is_enabled = is_enabled
        self_.message = message
        self_.name = name
        self_.options = options
        self_.queries = queries
