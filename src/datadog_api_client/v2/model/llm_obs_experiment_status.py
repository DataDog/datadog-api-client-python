# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsExperimentStatus(ModelSimple):
    """
    Execution status of an LLM Observability experiment.

    :param value: Must be one of ["running", "completed", "failed", "interrupted"].
    :type value: str
    """

    allowed_values = {
        "running",
        "completed",
        "failed",
        "interrupted",
    }
    RUNNING: ClassVar["LLMObsExperimentStatus"]
    COMPLETED: ClassVar["LLMObsExperimentStatus"]
    FAILED: ClassVar["LLMObsExperimentStatus"]
    INTERRUPTED: ClassVar["LLMObsExperimentStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsExperimentStatus.RUNNING = LLMObsExperimentStatus("running")
LLMObsExperimentStatus.COMPLETED = LLMObsExperimentStatus("completed")
LLMObsExperimentStatus.FAILED = LLMObsExperimentStatus("failed")
LLMObsExperimentStatus.INTERRUPTED = LLMObsExperimentStatus("interrupted")
