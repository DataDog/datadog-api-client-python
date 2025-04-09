# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_match_rule import (
        ObservabilityPipelineParseGrokProcessorRuleMatchRule,
    )
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_support_rule import (
        ObservabilityPipelineParseGrokProcessorRuleSupportRule,
    )


class ObservabilityPipelineParseGrokProcessorRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_match_rule import (
            ObservabilityPipelineParseGrokProcessorRuleMatchRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule_support_rule import (
            ObservabilityPipelineParseGrokProcessorRuleSupportRule,
        )

        return {
            "match_rules": ([ObservabilityPipelineParseGrokProcessorRuleMatchRule],),
            "source": (str,),
            "support_rules": ([ObservabilityPipelineParseGrokProcessorRuleSupportRule],),
        }

    attribute_map = {
        "match_rules": "match_rules",
        "source": "source",
        "support_rules": "support_rules",
    }

    def __init__(
        self_,
        match_rules: List[ObservabilityPipelineParseGrokProcessorRuleMatchRule],
        source: str,
        support_rules: List[ObservabilityPipelineParseGrokProcessorRuleSupportRule],
        **kwargs,
    ):
        """
        A grok parsing rule used in the ``parse_grok`` processor. Each rule defines how to extract structured fields
        from a specific log field using grok patterns.

        :param match_rules: A list of grok matching rules that define how to extract fields from the source field.
            Each rule must contain a name and a valid grok pattern.
        :type match_rules: [ObservabilityPipelineParseGrokProcessorRuleMatchRule]

        :param source: The name of the field in the log event to apply the grok rules to.
        :type source: str

        :param support_rules: A list of auxiliary Grok patterns that can be referenced by the matching rules.
            These are reusable named patterns that simplify complex matching.
        :type support_rules: [ObservabilityPipelineParseGrokProcessorRuleSupportRule]
        """
        super().__init__(kwargs)

        self_.match_rules = match_rules
        self_.source = source
        self_.support_rules = support_rules
