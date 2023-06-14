# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppPipelineEventPipelineLevel(ModelSimple):
    """
    Used to distinguish between pipelines, stages, jobs, and steps.

    :param value: If omitted defaults to "pipeline". Must be one of ["pipeline"].
    :type value: str
    """

    allowed_values = {
        "pipeline",
    }
    PIPELINE: ClassVar["CIAppPipelineEventPipelineLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppPipelineEventPipelineLevel.PIPELINE = CIAppPipelineEventPipelineLevel("pipeline")
