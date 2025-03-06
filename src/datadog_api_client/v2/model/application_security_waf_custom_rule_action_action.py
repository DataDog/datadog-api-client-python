# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleActionAction(ModelSimple):
    """
    Override the default action to take when the WAF custom rule would block.

    :param value: If omitted defaults to "block_request". Must be one of ["redirect_request", "block_request"].
    :type value: str
    """

    allowed_values = {
        "redirect_request",
        "block_request",
    }
    REDIRECT_REQUEST: ClassVar["ApplicationSecurityWafCustomRuleActionAction"]
    BLOCK_REQUEST: ClassVar["ApplicationSecurityWafCustomRuleActionAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleActionAction.REDIRECT_REQUEST = ApplicationSecurityWafCustomRuleActionAction(
    "redirect_request"
)
ApplicationSecurityWafCustomRuleActionAction.BLOCK_REQUEST = ApplicationSecurityWafCustomRuleActionAction(
    "block_request"
)
