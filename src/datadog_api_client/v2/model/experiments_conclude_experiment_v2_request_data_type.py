# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsConcludeExperimentV2RequestDataType(ModelSimple):
    """
    Conclude experiment request resource type.

    :param value: If omitted defaults to "conclude-experiment-request". Must be one of ["conclude-experiment-request"].
    :type value: str
    """

    allowed_values = {
        "conclude-experiment-request",
    }
    CONCLUDE_EXPERIMENT_REQUEST: ClassVar["ExperimentsConcludeExperimentV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsConcludeExperimentV2RequestDataType.CONCLUDE_EXPERIMENT_REQUEST = (
    ExperimentsConcludeExperimentV2RequestDataType("conclude-experiment-request")
)
