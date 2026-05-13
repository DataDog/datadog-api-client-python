# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListExecutionStepsDataType(ModelSimple):
    """
    The resource type for workflow execution steps.

    :param value: If omitted defaults to "workflow-execution-steps". Must be one of ["workflow-execution-steps"].
    :type value: str
    """

    allowed_values = {
        "workflow-execution-steps",
    }
    WORKFLOW_EXECUTION_STEPS: ClassVar["ListExecutionStepsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListExecutionStepsDataType.WORKFLOW_EXECUTION_STEPS = ListExecutionStepsDataType("workflow-execution-steps")
