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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_targeting_rules_items_conditions_items_operator import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator,
    )


class ExperimentsInlineCondition(ModelNormal):
    validations = {
        "attribute": {
            "min_length": 1,
        },
        "value": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_targeting_rules_items_conditions_items_operator import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator,
        )

        return {
            "attribute": (str,),
            "operator": (
                ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator,
            ),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "operator": "operator",
        "value": "value",
    }

    def __init__(
        self_,
        attribute: str,
        operator: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator,
        value: List[str],
        **kwargs,
    ):
        """
        An inline condition. The saved_filter_id field must be omitted or null.

        :param attribute: Attribute to evaluate.
        :type attribute: str

        :param operator: Required with attribute and value for an inline condition; omit when saved_filter_id is set.
        :type operator: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationTargetingRulesItemsConditionsItemsOperator

        :param value: Values used by the operator. Every operator requires at least one value.
        :type value: [str]
        """
        super().__init__(kwargs)

        self_.attribute = attribute
        self_.operator = operator
        self_.value = value
