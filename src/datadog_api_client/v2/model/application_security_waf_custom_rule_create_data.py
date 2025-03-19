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
    from datadog_api_client.v2.model.application_security_waf_custom_rule_create_attributes import (
        ApplicationSecurityWafCustomRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_type import (
        ApplicationSecurityWafCustomRuleType,
    )


class ApplicationSecurityWafCustomRuleCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_create_attributes import (
            ApplicationSecurityWafCustomRuleCreateAttributes,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_type import (
            ApplicationSecurityWafCustomRuleType,
        )

        return {
            "attributes": (ApplicationSecurityWafCustomRuleCreateAttributes,),
            "type": (ApplicationSecurityWafCustomRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ApplicationSecurityWafCustomRuleCreateAttributes,
        type: ApplicationSecurityWafCustomRuleType,
        **kwargs,
    ):
        """
        Object for a single WAF custom rule.

        :param attributes: Create a new WAF custom rule.
        :type attributes: ApplicationSecurityWafCustomRuleCreateAttributes

        :param type: The type of the resource. The value should always be ``custom_rule``.
        :type type: ApplicationSecurityWafCustomRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
