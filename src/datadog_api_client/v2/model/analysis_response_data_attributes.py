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
    from datadog_api_client.v2.model.analysis_rule_response import AnalysisRuleResponse


class AnalysisResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_rule_response import AnalysisRuleResponse

        return {
            "errors": ([str],),
            "rule_responses": ([AnalysisRuleResponse],),
        }

    attribute_map = {
        "errors": "errors",
        "rule_responses": "rule_responses",
    }

    def __init__(self_, errors: List[str], rule_responses: List[AnalysisRuleResponse], **kwargs):
        """
        The attributes of the analysis response, containing rule results and any top-level errors.

        :param errors: Top-level error messages encountered during the analysis operation.
        :type errors: [str]

        :param rule_responses: The list of results for each static analysis rule applied during analysis.
        :type rule_responses: [AnalysisRuleResponse]
        """
        super().__init__(kwargs)

        self_.errors = errors
        self_.rule_responses = rule_responses
