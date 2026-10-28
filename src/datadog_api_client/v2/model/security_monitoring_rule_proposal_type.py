# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleProposalType(ModelSimple):
    """
    The rule proposal resource type. The value is always `rule_proposals`.

    :param value: If omitted defaults to "rule_proposals". Must be one of ["rule_proposals"].
    :type value: str
    """

    allowed_values = {
        "rule_proposals",
    }
    RULE_PROPOSALS: ClassVar["SecurityMonitoringRuleProposalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleProposalType.RULE_PROPOSALS = SecurityMonitoringRuleProposalType("rule_proposals")
