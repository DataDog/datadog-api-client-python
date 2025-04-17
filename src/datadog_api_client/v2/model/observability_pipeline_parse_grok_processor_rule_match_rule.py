# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineParseGrokProcessorRuleMatchRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "rule": (str,),
        }

    attribute_map = {
        "name": "name",
        "rule": "rule",
    }

    def __init__(self_, name: str, rule: str, **kwargs):
        """
        Defines a Grok parsing rule, which extracts structured fields from log content using named Grok patterns.
        Each rule must have a unique name and a valid Datadog Grok pattern that will be applied to the source field.

        :param name: The name of the rule.
        :type name: str

        :param rule: The definition of the Grok rule.
        :type rule: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.rule = rule
