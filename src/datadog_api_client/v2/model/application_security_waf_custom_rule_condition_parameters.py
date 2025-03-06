# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input import (
        ApplicationSecurityWafCustomRuleConditionInput,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_options import (
        ApplicationSecurityWafCustomRuleConditionOptions,
    )


class ApplicationSecurityWafCustomRuleConditionParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input import (
            ApplicationSecurityWafCustomRuleConditionInput,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_options import (
            ApplicationSecurityWafCustomRuleConditionOptions,
        )

        return {
            "data": (str,),
            "inputs": ([ApplicationSecurityWafCustomRuleConditionInput],),
            "list": ([str],),
            "options": (ApplicationSecurityWafCustomRuleConditionOptions,),
            "regex": (str,),
            "value": (str,),
        }

    attribute_map = {
        "data": "data",
        "inputs": "inputs",
        "list": "list",
        "options": "options",
        "regex": "regex",
        "value": "value",
    }

    def __init__(
        self_,
        inputs: List[ApplicationSecurityWafCustomRuleConditionInput],
        data: Union[str, UnsetType] = unset,
        list: Union[List[str], UnsetType] = unset,
        options: Union[ApplicationSecurityWafCustomRuleConditionOptions, UnsetType] = unset,
        regex: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The scope of the WAF custom rule.

        :param data: Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.
        :type data: str, optional

        :param inputs: List of inputs on which at least one should match with the given operator.
        :type inputs: [ApplicationSecurityWafCustomRuleConditionInput]

        :param list: List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and
            !exact_match operator.
        :type list: [str], optional

        :param options: Options for the operator of this condition.
        :type options: ApplicationSecurityWafCustomRuleConditionOptions, optional

        :param regex: Regex to use with the condition. Only used with match_regex and !match_regex operator.
        :type regex: str, optional

        :param value: Store the captured value in the specified tag name. Only used with the capture_data operator.
        :type value: str, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if list is not unset:
            kwargs["list"] = list
        if options is not unset:
            kwargs["options"] = options
        if regex is not unset:
            kwargs["regex"] = regex
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.inputs = inputs
