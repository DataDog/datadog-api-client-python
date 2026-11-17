# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentOutreachRulesUpdateType(ModelSimple):
    """
    Type of an outreach policy rules update request.

    :param value: If omitted defaults to "outreach_policy_rules_update". Must be one of ["outreach_policy_rules_update"].
    :type value: str
    """

    allowed_values = {
        "outreach_policy_rules_update",
    }
    OUTREACH_POLICY_RULES_UPDATE: ClassVar["SecurityAgentOutreachRulesUpdateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentOutreachRulesUpdateType.OUTREACH_POLICY_RULES_UPDATE = SecurityAgentOutreachRulesUpdateType(
    "outreach_policy_rules_update"
)
