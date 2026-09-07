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
    from datadog_api_client.v2.model.security_monitoring_rule_user import SecurityMonitoringRuleUser
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_metadata import SecurityMonitoringRuleMetadata
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_signal_rule_response_query import (
        SecurityMonitoringSignalRuleResponseQuery,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_rule_type import SecurityMonitoringSignalRuleType


class SecurityMonitoringSignalRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
        from datadog_api_client.v2.model.security_monitoring_rule_user import SecurityMonitoringRuleUser
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_metadata import SecurityMonitoringRuleMetadata
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_signal_rule_response_query import (
            SecurityMonitoringSignalRuleResponseQuery,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_rule_type import SecurityMonitoringSignalRuleType

        return {
            "blocking": (bool,),
            "cases": ([SecurityMonitoringRuleCase],),
            "created_at": (int,),
            "creation_author_id": (int,),
            "creator": (SecurityMonitoringRuleUser,),
            "custom_message": (str,),
            "custom_name": (str,),
            "default_rule_id": (str,),
            "default_tags": ([str],),
            "deprecation_date": (int,),
            "filters": ([SecurityMonitoringFilter],),
            "has_extended_title": (bool,),
            "id": (str,),
            "is_beta": (bool,),
            "is_default": (bool,),
            "is_deleted": (bool,),
            "is_deprecated": (bool,),
            "is_enabled": (bool,),
            "is_partner": (bool,),
            "message": (str,),
            "metadata": (SecurityMonitoringRuleMetadata,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringSignalRuleResponseQuery],),
            "tags": ([str],),
            "type": (SecurityMonitoringSignalRuleType,),
            "update_author_id": (int,),
            "updated_at": (int,),
            "updater": (SecurityMonitoringRuleUser,),
            "version": (int,),
        }

    attribute_map = {
        "blocking": "blocking",
        "cases": "cases",
        "created_at": "createdAt",
        "creation_author_id": "creationAuthorId",
        "creator": "creator",
        "custom_message": "customMessage",
        "custom_name": "customName",
        "default_rule_id": "defaultRuleId",
        "default_tags": "defaultTags",
        "deprecation_date": "deprecationDate",
        "filters": "filters",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "is_beta": "isBeta",
        "is_default": "isDefault",
        "is_deleted": "isDeleted",
        "is_deprecated": "isDeprecated",
        "is_enabled": "isEnabled",
        "is_partner": "isPartner",
        "message": "message",
        "metadata": "metadata",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "tags": "tags",
        "type": "type",
        "update_author_id": "updateAuthorId",
        "updated_at": "updatedAt",
        "updater": "updater",
        "version": "version",
    }

    def __init__(
        self_,
        blocking: Union[bool, UnsetType] = unset,
        cases: Union[List[SecurityMonitoringRuleCase], UnsetType] = unset,
        created_at: Union[int, UnsetType] = unset,
        creation_author_id: Union[int, UnsetType] = unset,
        creator: Union[SecurityMonitoringRuleUser, UnsetType] = unset,
        custom_message: Union[str, UnsetType] = unset,
        custom_name: Union[str, UnsetType] = unset,
        default_rule_id: Union[str, UnsetType] = unset,
        default_tags: Union[List[str], UnsetType] = unset,
        deprecation_date: Union[int, UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        has_extended_title: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_beta: Union[bool, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        is_deleted: Union[bool, UnsetType] = unset,
        is_deprecated: Union[bool, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        is_partner: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        metadata: Union[SecurityMonitoringRuleMetadata, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        options: Union[SecurityMonitoringRuleOptions, UnsetType] = unset,
        queries: Union[List[SecurityMonitoringSignalRuleResponseQuery], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        type: Union[SecurityMonitoringSignalRuleType, UnsetType] = unset,
        update_author_id: Union[int, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updater: Union[SecurityMonitoringRuleUser, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Rule.

        :param blocking: Whether the rule blocks attackers.
        :type blocking: bool, optional

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCase], optional

        :param created_at: When the rule was created, timestamp in milliseconds.
        :type created_at: int, optional

        :param creation_author_id: User ID of the user who created the rule.
        :type creation_author_id: int, optional

        :param creator: The user who created or last updated the rule.
        :type creator: SecurityMonitoringRuleUser, optional

        :param custom_message: Custom/Overridden message for generated signals (used in case of Default rule update).
        :type custom_message: str, optional

        :param custom_name: Custom/Overridden name of the rule (used in case of Default rule update).
        :type custom_name: str, optional

        :param default_rule_id: The ID of the corresponding default rule.
        :type default_rule_id: str, optional

        :param default_tags: Default tags for default rules, included in tags.
        :type default_tags: [str], optional

        :param deprecation_date: When the rule will be deprecated, timestamp in milliseconds.
        :type deprecation_date: int, optional

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param id: The ID of the rule.
        :type id: str, optional

        :param is_beta: Whether the rule is in beta.
        :type is_beta: bool, optional

        :param is_default: Whether the rule is included by default.
        :type is_default: bool, optional

        :param is_deleted: Whether the rule has been deleted.
        :type is_deleted: bool, optional

        :param is_deprecated: Whether the rule is deprecated.
        :type is_deprecated: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool, optional

        :param is_partner: Whether the rule is provided by a partner.
        :type is_partner: bool, optional

        :param message: Message for generated signals.
        :type message: str, optional

        :param metadata: Metadata associated with the rule.
        :type metadata: SecurityMonitoringRuleMetadata, optional

        :param name: The name of the rule.
        :type name: str, optional

        :param options: Options.
        :type options: SecurityMonitoringRuleOptions, optional

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringSignalRuleResponseQuery], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param type: The rule type.
        :type type: SecurityMonitoringSignalRuleType, optional

        :param update_author_id: User ID of the user who updated the rule.
        :type update_author_id: int, optional

        :param updated_at: The date the rule was last updated, in milliseconds.
        :type updated_at: int, optional

        :param updater: The user who created or last updated the rule.
        :type updater: SecurityMonitoringRuleUser, optional

        :param version: The version of the rule.
        :type version: int, optional
        """
        if blocking is not unset:
            kwargs["blocking"] = blocking
        if cases is not unset:
            kwargs["cases"] = cases
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creation_author_id is not unset:
            kwargs["creation_author_id"] = creation_author_id
        if creator is not unset:
            kwargs["creator"] = creator
        if custom_message is not unset:
            kwargs["custom_message"] = custom_message
        if custom_name is not unset:
            kwargs["custom_name"] = custom_name
        if default_rule_id is not unset:
            kwargs["default_rule_id"] = default_rule_id
        if default_tags is not unset:
            kwargs["default_tags"] = default_tags
        if deprecation_date is not unset:
            kwargs["deprecation_date"] = deprecation_date
        if filters is not unset:
            kwargs["filters"] = filters
        if has_extended_title is not unset:
            kwargs["has_extended_title"] = has_extended_title
        if id is not unset:
            kwargs["id"] = id
        if is_beta is not unset:
            kwargs["is_beta"] = is_beta
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if is_deleted is not unset:
            kwargs["is_deleted"] = is_deleted
        if is_deprecated is not unset:
            kwargs["is_deprecated"] = is_deprecated
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if is_partner is not unset:
            kwargs["is_partner"] = is_partner
        if message is not unset:
            kwargs["message"] = message
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if name is not unset:
            kwargs["name"] = name
        if options is not unset:
            kwargs["options"] = options
        if queries is not unset:
            kwargs["queries"] = queries
        if tags is not unset:
            kwargs["tags"] = tags
        if type is not unset:
            kwargs["type"] = type
        if update_author_id is not unset:
            kwargs["update_author_id"] = update_author_id
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updater is not unset:
            kwargs["updater"] = updater
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
