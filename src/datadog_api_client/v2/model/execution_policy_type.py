# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExecutionPolicyType(ModelSimple):
    """
    The type of the resource. The value should always be `execution_policy`.

    :param value: If omitted defaults to "execution_policy". Must be one of ["execution_policy"].
    :type value: str
    """

    allowed_values = {
        "execution_policy",
    }
    EXECUTION_POLICY: ClassVar["ExecutionPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExecutionPolicyType.EXECUTION_POLICY = ExecutionPolicyType("execution_policy")
