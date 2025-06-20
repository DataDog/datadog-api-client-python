# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SecurityMonitoringRuleResponse(ModelComposed):
    def __init__(self, **kwargs):
        """
        Create a new rule.

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
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.security_monitoring_standard_rule_response import (
            SecurityMonitoringStandardRuleResponse,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_rule_response import (
            SecurityMonitoringSignalRuleResponse,
        )

        return {
            "oneOf": [
                SecurityMonitoringStandardRuleResponse,
                SecurityMonitoringSignalRuleResponse,
            ],
        }
