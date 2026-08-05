# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SeverityModifierRuleAction(ModelComposed):
    def __init__(self, **kwargs):
        """
        The action to take when a severity modifier rule matches a finding. This is a discriminated union on ``type`` : ``set`` assigns a fixed severity, while ``shift`` moves the severity up or down by one rank.

        A severity modifier rule's ``rule.query`` must not filter on ``@severity`` or on the ``@severity_details.user_adjusted.*`` namespace.

        Use ``@severity_details.adjusted.value`` instead, which reflects the severity before user-defined adjustments.

        :param description: An optional free-form explanation for the severity change.
        :type description: str, optional

        :param severity: The severity to assign to matched findings. `info_none` is not supported for the `iac_misconfiguration`, `runtime_code_vulnerability`, `secret`, or `static_code_vulnerability` finding types.
        :type severity: SeverityModifierSeverity

        :param type: The type of a severity modifier rule action that sets a fixed severity.
        :type type: SeverityModifierRuleSetActionType

        :param severity_delta: The direction in which to shift the severity of matched findings by one rank.
        :type severity_delta: SeverityModifierSeverityDelta
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
        from datadog_api_client.v2.model.severity_modifier_rule_set_action import SeverityModifierRuleSetAction
        from datadog_api_client.v2.model.severity_modifier_rule_shift_action import SeverityModifierRuleShiftAction

        return {
            "oneOf": [
                SeverityModifierRuleSetAction,
                SeverityModifierRuleShiftAction,
            ],
        }
