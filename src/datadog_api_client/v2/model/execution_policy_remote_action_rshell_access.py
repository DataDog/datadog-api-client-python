# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExecutionPolicyRemoteActionRshellAccess(ModelSimple):
    """
    The level of remote shell access granted for the target paths.

    :param value: Must be one of ["read_only", "read_write"].
    :type value: str
    """

    allowed_values = {
        "read_only",
        "read_write",
    }
    READ_ONLY: ClassVar["ExecutionPolicyRemoteActionRshellAccess"]
    READ_WRITE: ClassVar["ExecutionPolicyRemoteActionRshellAccess"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExecutionPolicyRemoteActionRshellAccess.READ_ONLY = ExecutionPolicyRemoteActionRshellAccess("read_only")
ExecutionPolicyRemoteActionRshellAccess.READ_WRITE = ExecutionPolicyRemoteActionRshellAccess("read_write")
