# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ExperimentsTargetingRuleCondition(ModelComposed):
    def __init__(self, **kwargs):
        """
        A saved-filter condition or a complete inline condition. The two forms cannot be combined.

        :param saved_filter_id: Saved-filter UUID.
        :type saved_filter_id: UUID

        :param attribute: Attribute to evaluate.
        :type attribute: str

        :param operator: Required with attribute and value for an inline condition; omit when saved_filter_id is set.
        :type operator: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator

        :param value: Values used by the operator. Every operator requires at least one value.
        :type value: [str]
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
        from datadog_api_client.v2.model.experiments_saved_filter_condition import ExperimentsSavedFilterCondition
        from datadog_api_client.v2.model.experiments_inline_condition import ExperimentsInlineCondition

        return {
            "oneOf": [
                ExperimentsSavedFilterCondition,
                ExperimentsInlineCondition,
            ],
        }
