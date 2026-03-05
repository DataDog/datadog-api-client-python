# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsExperimentSpanStatus(ModelSimple):
    """
    Status of the span.

    :param value: Must be one of ["ok", "error"].
    :type value: str
    """

    allowed_values = {
        "ok",
        "error",
    }
    OK: ClassVar["LLMObsExperimentSpanStatus"]
    ERROR: ClassVar["LLMObsExperimentSpanStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsExperimentSpanStatus.OK = LLMObsExperimentSpanStatus("ok")
LLMObsExperimentSpanStatus.ERROR = LLMObsExperimentSpanStatus("error")
