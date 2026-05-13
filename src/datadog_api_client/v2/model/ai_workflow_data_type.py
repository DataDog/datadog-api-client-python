# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIWorkflowDataType(ModelSimple):
    """
    The resource type for AI workflows.

    :param value: If omitted defaults to "ai-workflows". Must be one of ["ai-workflows"].
    :type value: str
    """

    allowed_values = {
        "ai-workflows",
    }
    AI_WORKFLOWS: ClassVar["AIWorkflowDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIWorkflowDataType.AI_WORKFLOWS = AIWorkflowDataType("ai-workflows")
