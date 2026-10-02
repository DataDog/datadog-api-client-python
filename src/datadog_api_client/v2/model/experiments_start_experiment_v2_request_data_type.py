# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsStartExperimentV2RequestDataType(ModelSimple):
    """
    Start experiment request resource type.

    :param value: If omitted defaults to "start-experiment-request". Must be one of ["start-experiment-request"].
    :type value: str
    """

    allowed_values = {
        "start-experiment-request",
    }
    START_EXPERIMENT_REQUEST: ClassVar["ExperimentsStartExperimentV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsStartExperimentV2RequestDataType.START_EXPERIMENT_REQUEST = ExperimentsStartExperimentV2RequestDataType(
    "start-experiment-request"
)
