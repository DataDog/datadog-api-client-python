# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_targeting_rule_condition import ExperimentsTargetingRuleCondition
    from datadog_api_client.v2.model.experiments_saved_filter_condition import ExperimentsSavedFilterCondition
    from datadog_api_client.v2.model.experiments_inline_condition import ExperimentsInlineCondition


class ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_targeting_rule_condition import ExperimentsTargetingRuleCondition

        return {
            "conditions": ([ExperimentsTargetingRuleCondition],),
        }

    attribute_map = {
        "conditions": "conditions",
    }

    def __init__(
        self_,
        conditions: List[
            Union[ExperimentsTargetingRuleCondition, ExperimentsSavedFilterCondition, ExperimentsInlineCondition]
        ],
        **kwargs,
    ):
        """
        Use an empty array when no targeting rules apply.

        :param conditions: Conditions that must all match for this rule. Each condition must use exactly one shape: saved_filter_id alone or operator plus attribute plus value.
        :type conditions: [ExperimentsTargetingRuleCondition]
        """
        super().__init__(kwargs)

        self_.conditions = conditions
