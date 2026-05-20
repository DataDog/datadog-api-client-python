# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RoutingRuleEscalationPolicyActionType(ModelSimple):
    """
    Indicates that the action pages an escalation policy. This action can be set once per routing rule item, and is mutually exclusive with the top-level `policy_id` field on the routing rule.

    :param value: If omitted defaults to "escalation_policy". Must be one of ["escalation_policy"].
    :type value: str
    """

    allowed_values = {
        "escalation_policy",
    }
    ESCALATION_POLICY: ClassVar["RoutingRuleEscalationPolicyActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RoutingRuleEscalationPolicyActionType.ESCALATION_POLICY = RoutingRuleEscalationPolicyActionType("escalation_policy")
