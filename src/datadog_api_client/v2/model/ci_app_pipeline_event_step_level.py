# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CIAppPipelineEventStepLevel(StringEnum):
    """
    Used to distinguish between pipelines, stages, jobs and steps.

    :param value: If omitted defaults to "step". Must be one of ["step"].
    :type value: str
    """

    allowed_values = {
        "step",
    }
    STEP: ClassVar["CIAppPipelineEventStepLevel"]


CIAppPipelineEventStepLevel.STEP = CIAppPipelineEventStepLevel("step")
