# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_waf_custom_rule_action_action import (
        ApplicationSecurityWafCustomRuleActionAction,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_action_parameters import (
        ApplicationSecurityWafCustomRuleActionParameters,
    )


class ApplicationSecurityWafCustomRuleAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_action_action import (
            ApplicationSecurityWafCustomRuleActionAction,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_action_parameters import (
            ApplicationSecurityWafCustomRuleActionParameters,
        )

        return {
            "action": (ApplicationSecurityWafCustomRuleActionAction,),
            "parameters": (ApplicationSecurityWafCustomRuleActionParameters,),
        }

    attribute_map = {
        "action": "action",
        "parameters": "parameters",
    }

    def __init__(
        self_,
        action: Union[ApplicationSecurityWafCustomRuleActionAction, UnsetType] = unset,
        parameters: Union[ApplicationSecurityWafCustomRuleActionParameters, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ApplicationSecurityWafCustomRuleAction`` object.

        :param action: Override the default action to take when the WAF custom rule would block.
        :type action: ApplicationSecurityWafCustomRuleActionAction, optional

        :param parameters: The definition of ``ApplicationSecurityWafCustomRuleActionParameters`` object.
        :type parameters: ApplicationSecurityWafCustomRuleActionParameters, optional
        """
        if action is not unset:
            kwargs["action"] = action
        if parameters is not unset:
            kwargs["parameters"] = parameters
        super().__init__(kwargs)
