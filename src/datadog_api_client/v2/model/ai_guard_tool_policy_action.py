# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIGuardToolPolicyAction(ModelSimple):
    """
    The policy action for a tool named by the property. Tool policies override
        the recommendation after evaluation; they do not skip evaluation.
        Any BLOCK takes precedence over PASS and EVALUATE. The Supply Chain Firewall
        is applied afterward and can still return DENY.

    :param value: Must be one of ["PASS", "BLOCK", "EVALUATE"].
    :type value: str
    """

    allowed_values = {
        "PASS",
        "BLOCK",
        "EVALUATE",
    }
    PASS: ClassVar["AIGuardToolPolicyAction"]
    BLOCK: ClassVar["AIGuardToolPolicyAction"]
    EVALUATE: ClassVar["AIGuardToolPolicyAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIGuardToolPolicyAction.PASS = AIGuardToolPolicyAction("PASS")
AIGuardToolPolicyAction.BLOCK = AIGuardToolPolicyAction("BLOCK")
AIGuardToolPolicyAction.EVALUATE = AIGuardToolPolicyAction("EVALUATE")
