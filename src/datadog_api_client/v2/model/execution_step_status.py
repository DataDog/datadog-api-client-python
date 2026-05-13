# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExecutionStepStatus(ModelSimple):
    """
    The current status of the step.

    :param value: Must be one of ["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELED"].
    :type value: str
    """

    allowed_values = {
        "PENDING",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "CANCELED",
    }
    PENDING: ClassVar["ExecutionStepStatus"]
    RUNNING: ClassVar["ExecutionStepStatus"]
    COMPLETED: ClassVar["ExecutionStepStatus"]
    FAILED: ClassVar["ExecutionStepStatus"]
    CANCELED: ClassVar["ExecutionStepStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExecutionStepStatus.PENDING = ExecutionStepStatus("PENDING")
ExecutionStepStatus.RUNNING = ExecutionStepStatus("RUNNING")
ExecutionStepStatus.COMPLETED = ExecutionStepStatus("COMPLETED")
ExecutionStepStatus.FAILED = ExecutionStepStatus("FAILED")
ExecutionStepStatus.CANCELED = ExecutionStepStatus("CANCELED")
