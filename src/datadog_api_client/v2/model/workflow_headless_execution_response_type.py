# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WorkflowHeadlessExecutionResponseType(ModelSimple):
    """
    The type for workflow headless execution response

    :param value: If omitted defaults to "workflow_headless_execution". Must be one of ["workflow_headless_execution"].
    :type value: str
    """

    allowed_values = {
        "workflow_headless_execution",
    }
    WORKFLOW_HEADLESS_EXECUTION: ClassVar["WorkflowHeadlessExecutionResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WorkflowHeadlessExecutionResponseType.WORKFLOW_HEADLESS_EXECUTION = WorkflowHeadlessExecutionResponseType(
    "workflow_headless_execution"
)
