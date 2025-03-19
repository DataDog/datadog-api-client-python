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
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input_address import (
        ApplicationSecurityWafCustomRuleConditionInputAddress,
    )


class ApplicationSecurityWafCustomRuleConditionInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input_address import (
            ApplicationSecurityWafCustomRuleConditionInputAddress,
        )

        return {
            "address": (ApplicationSecurityWafCustomRuleConditionInputAddress,),
            "key_path": ([str],),
        }

    attribute_map = {
        "address": "address",
        "key_path": "key_path",
    }

    def __init__(
        self_,
        address: ApplicationSecurityWafCustomRuleConditionInputAddress,
        key_path: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Input from the request on which the condition should apply.

        :param address: Input from the request on which the condition should apply.
        :type address: ApplicationSecurityWafCustomRuleConditionInputAddress

        :param key_path: Specific path for the input.
        :type key_path: [str], optional
        """
        if key_path is not unset:
            kwargs["key_path"] = key_path
        super().__init__(kwargs)

        self_.address = address
