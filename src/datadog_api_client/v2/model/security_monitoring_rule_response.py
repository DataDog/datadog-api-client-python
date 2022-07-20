# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery
        from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead

        return {
            "cases": ([SecurityMonitoringRuleCase],),
            "created_at": (int,),
            "creation_author_id": (int,),
            "filters": ([SecurityMonitoringFilter],),
            "has_extended_title": (bool,),
            "id": (str,),
            "is_default": (bool,),
            "is_deleted": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringRuleQuery],),
            "tags": ([str],),
            "type": (SecurityMonitoringRuleTypeRead,),
            "update_author_id": (int,),
            "version": (int,),
        }

    attribute_map = {
        "cases": "cases",
        "created_at": "createdAt",
        "creation_author_id": "creationAuthorId",
        "filters": "filters",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "is_default": "isDefault",
        "is_deleted": "isDeleted",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "tags": "tags",
        "type": "type",
        "update_author_id": "updateAuthorId",
        "version": "version",
    }

    def __init__(self, *args, **kwargs):
        """
        Rule.

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCase], optional

        :param created_at: When the rule was created, timestamp in milliseconds.
        :type created_at: int, optional

        :param creation_author_id: User ID of the user who created the rule.
        :type creation_author_id: int, optional

        :param filters: Additional queries to filter matched events before they are processed.
        :type filters: [SecurityMonitoringFilter], optional

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

        :param options: Options on rules.
        :type options: SecurityMonitoringRuleOptions, optional

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringRuleQuery], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param type: The rule type.
        :type type: SecurityMonitoringRuleTypeRead, optional

        :param update_author_id: User ID of the user who updated the rule.
        :type update_author_id: int, optional

        :param version: The version of the rule.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
