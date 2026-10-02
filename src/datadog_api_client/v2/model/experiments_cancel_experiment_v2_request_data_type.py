# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsCancelExperimentV2RequestDataType(ModelSimple):
    """
    Cancel experiment request resource type.

    :param value: If omitted defaults to "cancel-experiment-request". Must be one of ["cancel-experiment-request"].
    :type value: str
    """

    allowed_values = {
        "cancel-experiment-request",
    }
    CANCEL_EXPERIMENT_REQUEST: ClassVar["ExperimentsCancelExperimentV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsCancelExperimentV2RequestDataType.CANCEL_EXPERIMENT_REQUEST = ExperimentsCancelExperimentV2RequestDataType(
    "cancel-experiment-request"
)
