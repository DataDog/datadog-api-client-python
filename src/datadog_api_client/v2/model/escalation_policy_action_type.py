# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EscalationPolicyActionType(ModelSimple):
    """
    Indicates that the action is an escalation policy action.

    :param value: If omitted defaults to "escalation_policy". Must be one of ["escalation_policy"].
    :type value: str
    """

    allowed_values = {
        "escalation_policy",
    }
    ESCALATION_POLICY: ClassVar["EscalationPolicyActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EscalationPolicyActionType.ESCALATION_POLICY = EscalationPolicyActionType("escalation_policy")
