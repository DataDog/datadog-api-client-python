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
    from datadog_api_client.v2.model.issue_type import IssueType
    from datadog_api_client.v2.model.security_rule_types_items import SecurityRuleTypesItems
    from datadog_api_client.v2.model.security_rule_severity import SecurityRuleSeverity


class AutomationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_type import IssueType
        from datadog_api_client.v2.model.security_rule_types_items import SecurityRuleTypesItems
        from datadog_api_client.v2.model.security_rule_severity import SecurityRuleSeverity

        return {
            "issue_type": (IssueType,),
            "query": (str,),
            "rule_ids": ([str],),
            "rule_types": ([SecurityRuleTypesItems],),
            "severities": ([SecurityRuleSeverity],),
        }

    attribute_map = {
        "issue_type": "issue_type",
        "query": "query",
        "rule_ids": "rule_ids",
        "rule_types": "rule_types",
        "severities": "severities",
    }

    def __init__(
        self_,
        issue_type: IssueType,
        rule_types: List[SecurityRuleTypesItems],
        query: Union[str, UnsetType] = unset,
        rule_ids: Union[List[str], UnsetType] = unset,
        severities: Union[List[SecurityRuleSeverity], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of an automation pipeline rule scope.
        A rule can act on specific issue types, security rule types, security rule IDs, rule severities, or a query.
        The query can be used to filter resources on tags and attributes.
        The issue type and rule types fields are required.

        :param issue_type: The type of issues on which the rule applies
        :type issue_type: IssueType

        :param query: The query is composed of one or several key:value pairs, which can be used to filter resources on tags and attributes.
        :type query: str, optional

        :param rule_ids: Security rule ids
        :type rule_ids: [str], optional

        :param rule_types: Security rule types
        :type rule_types: [SecurityRuleTypesItems]

        :param severities: The security rules severities to consider
        :type severities: [SecurityRuleSeverity], optional
        """
        if query is not unset:
            kwargs["query"] = query
        if rule_ids is not unset:
            kwargs["rule_ids"] = rule_ids
        if severities is not unset:
            kwargs["severities"] = severities
        super().__init__(kwargs)

        self_.issue_type = issue_type
        self_.rule_types = rule_types
