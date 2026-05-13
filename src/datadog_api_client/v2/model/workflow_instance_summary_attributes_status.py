# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WorkflowInstanceSummaryAttributesStatus(ModelSimple):
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
    PENDING: ClassVar["WorkflowInstanceSummaryAttributesStatus"]
    RUNNING: ClassVar["WorkflowInstanceSummaryAttributesStatus"]
    COMPLETED: ClassVar["WorkflowInstanceSummaryAttributesStatus"]
    FAILED: ClassVar["WorkflowInstanceSummaryAttributesStatus"]
    CANCELED: ClassVar["WorkflowInstanceSummaryAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WorkflowInstanceSummaryAttributesStatus.PENDING = WorkflowInstanceSummaryAttributesStatus("PENDING")
WorkflowInstanceSummaryAttributesStatus.RUNNING = WorkflowInstanceSummaryAttributesStatus("RUNNING")
WorkflowInstanceSummaryAttributesStatus.COMPLETED = WorkflowInstanceSummaryAttributesStatus("COMPLETED")
WorkflowInstanceSummaryAttributesStatus.FAILED = WorkflowInstanceSummaryAttributesStatus("FAILED")
WorkflowInstanceSummaryAttributesStatus.CANCELED = WorkflowInstanceSummaryAttributesStatus("CANCELED")
