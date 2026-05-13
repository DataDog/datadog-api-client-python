# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListPROutputsDataType(ModelSimple):
    """
    The resource type for workflow execution PR outputs.

    :param value: If omitted defaults to "workflow-execution-pr-outputs". Must be one of ["workflow-execution-pr-outputs"].
    :type value: str
    """

    allowed_values = {
        "workflow-execution-pr-outputs",
    }
    WORKFLOW_EXECUTION_PR_OUTPUTS: ClassVar["ListPROutputsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListPROutputsDataType.WORKFLOW_EXECUTION_PR_OUTPUTS = ListPROutputsDataType("workflow-execution-pr-outputs")
