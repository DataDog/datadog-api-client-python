# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineParseGrokProcessorRuleSupportRule(ModelNormal):
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
        The Grok helper rule referenced in the parsing rules.

        :param name: The name of the Grok helper rule.
        :type name: str

        :param rule: The definition of the Grok helper rule.
        :type rule: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.rule = rule
