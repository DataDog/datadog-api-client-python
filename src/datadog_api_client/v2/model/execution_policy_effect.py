# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExecutionPolicyEffect(ModelSimple):
    """
    Whether the policy allows or denies matching actions.

    :param value: Must be one of ["allow", "deny"].
    :type value: str
    """

    allowed_values = {
        "allow",
        "deny",
    }
    ALLOW: ClassVar["ExecutionPolicyEffect"]
    DENY: ClassVar["ExecutionPolicyEffect"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExecutionPolicyEffect.ALLOW = ExecutionPolicyEffect("allow")
ExecutionPolicyEffect.DENY = ExecutionPolicyEffect("deny")
