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
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_match_rule import (
        ObservabilityPipelineParseGrokProcessorRuleMatchRule,
    )
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_support_rule import (
        ObservabilityPipelineParseGrokProcessorRuleSupportRule,
    )


class ObservabilityPipelineParseGrokProcessorIncludeRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_match_rule import (
            ObservabilityPipelineParseGrokProcessorRuleMatchRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_support_rule import (
            ObservabilityPipelineParseGrokProcessorRuleSupportRule,
        )

        return {
            "include": (str,),
            "match_rules": ([ObservabilityPipelineParseGrokProcessorRuleMatchRule],),
            "support_rules": ([ObservabilityPipelineParseGrokProcessorRuleSupportRule],),
        }

    attribute_map = {
        "include": "include",
        "match_rules": "match_rules",
        "support_rules": "support_rules",
    }

    def __init__(
        self_,
        include: str,
        match_rules: List[ObservabilityPipelineParseGrokProcessorRuleMatchRule],
        support_rules: Union[List[ObservabilityPipelineParseGrokProcessorRuleSupportRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        A Grok parsing rule selected using the ``include`` query. Each rule defines how to extract structured fields
        from logs matching a Datadog search query.

        :param include: A Datadog search query used to determine which logs this Grok rule targets.
        :type include: str

        :param match_rules: A list of Grok parsing rules that define how to extract fields from matching logs.
            Each rule must contain a name and a valid Grok pattern.
        :type match_rules: [ObservabilityPipelineParseGrokProcessorRuleMatchRule]

        :param support_rules: A list of Grok helper rules that can be referenced by the parsing rules.
        :type support_rules: [ObservabilityPipelineParseGrokProcessorRuleSupportRule], optional
        """
        if support_rules is not unset:
            kwargs["support_rules"] = support_rules
        super().__init__(kwargs)

        self_.include = include
        self_.match_rules = match_rules
