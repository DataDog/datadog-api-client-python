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
    from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
        ApplicationSecurityWafCustomRuleTagsCategory,
    )


class ApplicationSecurityWafCustomRuleTags(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
            ApplicationSecurityWafCustomRuleTagsCategory,
        )

        return {
            "category": (ApplicationSecurityWafCustomRuleTagsCategory,),
            "type": (str,),
        }

    attribute_map = {
        "category": "category",
        "type": "type",
    }

    def __init__(self_, category: ApplicationSecurityWafCustomRuleTagsCategory, type: str, **kwargs):
        """
        Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security
        activity field associated with the traces.

        :param category: The category of the WAF Rule, can be either ``business_logic`` , ``attack_attempt`` or ``security_response``.
        :type category: ApplicationSecurityWafCustomRuleTagsCategory

        :param type: The type of the WAF rule, associated with the category will form the security activity.
        :type type: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.type = type
