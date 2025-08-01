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
    from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
    from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
    from datadog_api_client.v2.model.security_monitoring_third_party_rule_case import (
        SecurityMonitoringThirdPartyRuleCase,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead


class SecurityMonitoringStandardRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
        from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
            CloudConfigurationRuleComplianceSignalOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_standard_rule_query import (
            SecurityMonitoringStandardRuleQuery,
        )
        from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
        from datadog_api_client.v2.model.security_monitoring_third_party_rule_case import (
            SecurityMonitoringThirdPartyRuleCase,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead

        return {
            "cases": ([SecurityMonitoringRuleCase],),
            "compliance_signal_options": (CloudConfigurationRuleComplianceSignalOptions,),
            "created_at": (int,),
            "creation_author_id": (int,),
            "custom_message": (str,),
            "custom_name": (str,),
            "default_tags": ([str],),
            "deprecation_date": (int,),
            "filters": ([SecurityMonitoringFilter],),
            "group_signals_by": ([str],),
            "has_extended_title": (bool,),
            "id": (str,),
            "is_default": (bool,),
            "is_deleted": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringStandardRuleQuery],),
            "reference_tables": ([SecurityMonitoringReferenceTable],),
            "tags": ([str],),
            "third_party_cases": ([SecurityMonitoringThirdPartyRuleCase],),
            "type": (SecurityMonitoringRuleTypeRead,),
            "update_author_id": (int,),
            "updated_at": (int,),
            "version": (int,),
        }

    attribute_map = {
        "cases": "cases",
        "compliance_signal_options": "complianceSignalOptions",
        "created_at": "createdAt",
        "creation_author_id": "creationAuthorId",
        "custom_message": "customMessage",
        "custom_name": "customName",
        "default_tags": "defaultTags",
        "deprecation_date": "deprecationDate",
        "filters": "filters",
        "group_signals_by": "groupSignalsBy",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "is_default": "isDefault",
        "is_deleted": "isDeleted",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "reference_tables": "referenceTables",
        "tags": "tags",
        "third_party_cases": "thirdPartyCases",
        "type": "type",
        "update_author_id": "updateAuthorId",
        "updated_at": "updatedAt",
        "version": "version",
    }

    def __init__(
        self_,
        cases: Union[List[SecurityMonitoringRuleCase], UnsetType] = unset,
        compliance_signal_options: Union[CloudConfigurationRuleComplianceSignalOptions, UnsetType] = unset,
        created_at: Union[int, UnsetType] = unset,
        creation_author_id: Union[int, UnsetType] = unset,
        custom_message: Union[str, UnsetType] = unset,
        custom_name: Union[str, UnsetType] = unset,
        default_tags: Union[List[str], UnsetType] = unset,
        deprecation_date: Union[int, UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        group_signals_by: Union[List[str], UnsetType] = unset,
        has_extended_title: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        is_deleted: Union[bool, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        options: Union[SecurityMonitoringRuleOptions, UnsetType] = unset,
        queries: Union[List[SecurityMonitoringStandardRuleQuery], UnsetType] = unset,
        reference_tables: Union[List[SecurityMonitoringReferenceTable], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        third_party_cases: Union[List[SecurityMonitoringThirdPartyRuleCase], UnsetType] = unset,
        type: Union[SecurityMonitoringRuleTypeRead, UnsetType] = unset,
        update_author_id: Union[int, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Rule.

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCase], optional

        :param compliance_signal_options: How to generate compliance signals. Useful for cloud_configuration rules only.
        :type compliance_signal_options: CloudConfigurationRuleComplianceSignalOptions, optional

        :param created_at: When the rule was created, timestamp in milliseconds.
        :type created_at: int, optional

        :param creation_author_id: User ID of the user who created the rule.
        :type creation_author_id: int, optional

        :param custom_message: Custom/Overridden message for generated signals (used in case of Default rule update).
        :type custom_message: str, optional

        :param custom_name: Custom/Overridden name of the rule (used in case of Default rule update).
        :type custom_name: str, optional

        :param default_tags: Default Tags for default rules (included in tags)
        :type default_tags: [str], optional

        :param deprecation_date: When the rule will be deprecated, timestamp in milliseconds.
        :type deprecation_date: int, optional

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param group_signals_by: Additional grouping to perform on top of the existing groups in the query section. Must be a subset of the existing groups.
        :type group_signals_by: [str], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param id: The ID of the rule.
        :type id: str, optional

        :param is_default: Whether the rule is included by default.
        :type is_default: bool, optional

        :param is_deleted: Whether the rule has been deleted.
        :type is_deleted: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool, optional

        :param message: Message for generated signals.
        :type message: str, optional

        :param name: The name of the rule.
        :type name: str, optional

        :param options: Options.
        :type options: SecurityMonitoringRuleOptions, optional

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringStandardRuleQuery], optional

        :param reference_tables: Reference tables for the rule.
        :type reference_tables: [SecurityMonitoringReferenceTable], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param third_party_cases: Cases for generating signals from third-party rules. Only available for third-party rules.
        :type third_party_cases: [SecurityMonitoringThirdPartyRuleCase], optional

        :param type: The rule type.
        :type type: SecurityMonitoringRuleTypeRead, optional

        :param update_author_id: User ID of the user who updated the rule.
        :type update_author_id: int, optional

        :param updated_at: The date the rule was last updated, in milliseconds.
        :type updated_at: int, optional

        :param version: The version of the rule.
        :type version: int, optional
        """
        if cases is not unset:
            kwargs["cases"] = cases
        if compliance_signal_options is not unset:
            kwargs["compliance_signal_options"] = compliance_signal_options
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creation_author_id is not unset:
            kwargs["creation_author_id"] = creation_author_id
        if custom_message is not unset:
            kwargs["custom_message"] = custom_message
        if custom_name is not unset:
            kwargs["custom_name"] = custom_name
        if default_tags is not unset:
            kwargs["default_tags"] = default_tags
        if deprecation_date is not unset:
            kwargs["deprecation_date"] = deprecation_date
        if filters is not unset:
            kwargs["filters"] = filters
        if group_signals_by is not unset:
            kwargs["group_signals_by"] = group_signals_by
        if has_extended_title is not unset:
            kwargs["has_extended_title"] = has_extended_title
        if id is not unset:
            kwargs["id"] = id
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if is_deleted is not unset:
            kwargs["is_deleted"] = is_deleted
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
        if type is not unset:
            kwargs["type"] = type
        if update_author_id is not unset:
            kwargs["update_author_id"] = update_author_id
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
