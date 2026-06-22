# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationWorkloadType(ModelSimple):
    """
    The kind of ECS workload that owns the problematic tasks.

    :param value: Must be one of ["WORKLOAD_TYPE_UNSPECIFIED", "SERVICE", "STANDALONE_TASK", "DAEMON"].
    :type value: str
    """

    allowed_values = {
        "WORKLOAD_TYPE_UNSPECIFIED",
        "SERVICE",
        "STANDALONE_TASK",
        "DAEMON",
    }
    WORKLOAD_TYPE_UNSPECIFIED: ClassVar["RemediationWorkloadType"]
    SERVICE: ClassVar["RemediationWorkloadType"]
    STANDALONE_TASK: ClassVar["RemediationWorkloadType"]
    DAEMON: ClassVar["RemediationWorkloadType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationWorkloadType.WORKLOAD_TYPE_UNSPECIFIED = RemediationWorkloadType("WORKLOAD_TYPE_UNSPECIFIED")
RemediationWorkloadType.SERVICE = RemediationWorkloadType("SERVICE")
RemediationWorkloadType.STANDALONE_TASK = RemediationWorkloadType("STANDALONE_TASK")
RemediationWorkloadType.DAEMON = RemediationWorkloadType("DAEMON")
