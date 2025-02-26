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
    from datadog_api_client.v2.model.application_security_waf_custom_rule_update_data import (
        ApplicationSecurityWafCustomRuleUpdateData,
    )


class ApplicationSecurityWafCustomRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_update_data import (
            ApplicationSecurityWafCustomRuleUpdateData,
        )

        return {
            "data": (ApplicationSecurityWafCustomRuleUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ApplicationSecurityWafCustomRuleUpdateData, **kwargs):
        """
        Request object that includes the Custom Rule to update.

        :param data: Object for a single WAF Custom Rule.
        :type data: ApplicationSecurityWafCustomRuleUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
