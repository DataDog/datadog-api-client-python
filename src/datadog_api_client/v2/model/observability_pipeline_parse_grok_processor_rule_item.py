# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineParseGrokProcessorRuleItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A single Grok parsing rule, selected by either source field or include query.

        :param match_rules: A list of Grok parsing rules that define how to extract fields from the source field.
            Each rule must contain a name and a valid Grok pattern.
        :type match_rules: [ObservabilityPipelineParseGrokProcessorRuleMatchRule]

        :param source: The value of the source field in log events to be processed by the Grok rules.
        :type source: str

        :param support_rules: A list of Grok helper rules that can be referenced by the parsing rules.
        :type support_rules: [ObservabilityPipelineParseGrokProcessorRuleSupportRule], optional

        :param include: A Datadog search query used to determine which logs this Grok rule targets.
        :type include: str
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
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule import (
            ObservabilityPipelineParseGrokProcessorRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_include_rule import (
            ObservabilityPipelineParseGrokProcessorIncludeRule,
        )

        return {
            "oneOf": [
                ObservabilityPipelineParseGrokProcessorRule,
                ObservabilityPipelineParseGrokProcessorIncludeRule,
            ],
        }
