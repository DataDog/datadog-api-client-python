# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_operator import (
        ApplicationSecurityWafCustomRuleConditionOperator,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
        ApplicationSecurityWafCustomRuleConditionParameters,
    )


class ApplicationSecurityWafCustomRuleCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_operator import (
            ApplicationSecurityWafCustomRuleConditionOperator,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
            ApplicationSecurityWafCustomRuleConditionParameters,
        )

        return {
            "operator": (ApplicationSecurityWafCustomRuleConditionOperator,),
            "parameters": (ApplicationSecurityWafCustomRuleConditionParameters,),
        }

    attribute_map = {
        "operator": "operator",
        "parameters": "parameters",
    }

    def __init__(
        self_,
        operator: ApplicationSecurityWafCustomRuleConditionOperator,
        parameters: ApplicationSecurityWafCustomRuleConditionParameters,
        **kwargs,
    ):
        """
        One condition of the WAF Custom Rule.

        :param operator: Operator to use for the WAF Condition.
        :type operator: ApplicationSecurityWafCustomRuleConditionOperator

        :param parameters: The scope of the WAF custom rule.
        :type parameters: ApplicationSecurityWafCustomRuleConditionParameters
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.parameters = parameters
