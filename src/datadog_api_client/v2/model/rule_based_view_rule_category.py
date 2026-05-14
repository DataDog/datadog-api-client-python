# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RuleBasedViewRuleCategory(ModelSimple):
    """
    The category of the security rule.

    :param value: Must be one of ["cloud_configuration", "infrastructure_configuration", "api_security"].
    :type value: str
    """

    allowed_values = {
        "cloud_configuration",
        "infrastructure_configuration",
        "api_security",
    }
    CLOUD_CONFIGURATION: ClassVar["RuleBasedViewRuleCategory"]
    INFRASTRUCTURE_CONFIGURATION: ClassVar["RuleBasedViewRuleCategory"]
    API_SECURITY: ClassVar["RuleBasedViewRuleCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RuleBasedViewRuleCategory.CLOUD_CONFIGURATION = RuleBasedViewRuleCategory("cloud_configuration")
RuleBasedViewRuleCategory.INFRASTRUCTURE_CONFIGURATION = RuleBasedViewRuleCategory("infrastructure_configuration")
RuleBasedViewRuleCategory.API_SECURITY = RuleBasedViewRuleCategory("api_security")
