# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppPipelineLevel(ModelSimple):
    """
    Pipeline execution level.

    :param value: Must be one of ["pipeline", "stage", "job", "step", "custom"].
    :type value: str
    """

    allowed_values = {
        "pipeline",
        "stage",
        "job",
        "step",
        "custom",
    }
    PIPELINE: ClassVar["CIAppPipelineLevel"]
    STAGE: ClassVar["CIAppPipelineLevel"]
    JOB: ClassVar["CIAppPipelineLevel"]
    STEP: ClassVar["CIAppPipelineLevel"]
    CUSTOM: ClassVar["CIAppPipelineLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppPipelineLevel.PIPELINE = CIAppPipelineLevel("pipeline")
CIAppPipelineLevel.STAGE = CIAppPipelineLevel("stage")
CIAppPipelineLevel.JOB = CIAppPipelineLevel("job")
CIAppPipelineLevel.STEP = CIAppPipelineLevel("step")
CIAppPipelineLevel.CUSTOM = CIAppPipelineLevel("custom")
