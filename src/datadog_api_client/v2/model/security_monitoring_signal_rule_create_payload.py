# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalRuleCreatePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_signal_rule_query import SecurityMonitoringSignalRuleQuery
        from datadog_api_client.v2.model.security_monitoring_signal_rule_type import SecurityMonitoringSignalRuleType

        return {
            "cases": ([SecurityMonitoringRuleCaseCreate],),
            "filters": ([SecurityMonitoringFilter],),
            "has_extended_title": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringSignalRuleQuery],),
            "tags": ([str],),
            "type": (SecurityMonitoringSignalRuleType,),
        }

    attribute_map = {
        "cases": "cases",
        "filters": "filters",
        "has_extended_title": "hasExtendedTitle",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "tags": "tags",
        "type": "type",
    }

    def __init__(self_, cases, is_enabled, message, name, options, queries, *args, **kwargs):
        """
        Create a new signal correlation rule.

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCaseCreate]

        :param filters: Additional queries to filter matched events before they are processed.
        :type filters: [SecurityMonitoringFilter], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool

        :param message: Message for generated signals.
        :type message: str

        :param name: The name of the rule.
        :type name: str

        :param options: Options on rules.
        :type options: SecurityMonitoringRuleOptions

        :param queries: Queries for selecting signals which are part of the rule.
        :type queries: [SecurityMonitoringSignalRuleQuery]

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param type: The rule type.
        :type type: SecurityMonitoringSignalRuleType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.cases = cases
        self_.is_enabled = is_enabled
        self_.message = message
        self_.name = name
        self_.options = options
        self_.queries = queries
