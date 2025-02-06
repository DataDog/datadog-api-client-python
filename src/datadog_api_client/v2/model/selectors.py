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
    from datadog_api_client.v2.model.rule_types_items import RuleTypesItems
    from datadog_api_client.v2.model.rule_severity import RuleSeverity
    from datadog_api_client.v2.model.trigger_source import TriggerSource


class Selectors(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_types_items import RuleTypesItems
        from datadog_api_client.v2.model.rule_severity import RuleSeverity
        from datadog_api_client.v2.model.trigger_source import TriggerSource

        return {
            "query": (str,),
            "rule_types": ([RuleTypesItems],),
            "severities": ([RuleSeverity],),
            "trigger_source": (TriggerSource,),
        }

    attribute_map = {
        "query": "query",
        "rule_types": "rule_types",
        "severities": "severities",
        "trigger_source": "trigger_source",
    }

    def __init__(
        self_,
        trigger_source: TriggerSource,
        query: Union[str, UnsetType] = unset,
        rule_types: Union[List[RuleTypesItems], UnsetType] = unset,
        severities: Union[List[RuleSeverity], UnsetType] = unset,
        **kwargs,
    ):
        """
        Selectors are used to filter security issues for which notifications should be generated.
        Users can specify rule severities, rule types, a query to filter security issues on tags and attributes, and the trigger source.
        Only the trigger_source field is required.

        :param query: The query is composed of one or several key:value pairs, which can be used to filter security issues on tags and attributes.
        :type query: str, optional

        :param rule_types: Security rule types used as filters in security rules.
        :type rule_types: [RuleTypesItems], optional

        :param severities: The security rules severities to consider.
        :type severities: [RuleSeverity], optional

        :param trigger_source: The type of security issues on which the rule applies. Notification rules based on security signals need to use the trigger source "security_signals",
            while notification rules based on security vulnerabilities need to use the trigger source "security_findings".
        :type trigger_source: TriggerSource
        """
        if query is not unset:
            kwargs["query"] = query
        if rule_types is not unset:
            kwargs["rule_types"] = rule_types
        if severities is not unset:
            kwargs["severities"] = severities
        super().__init__(kwargs)

        self_.trigger_source = trigger_source
