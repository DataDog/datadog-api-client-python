# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsPatchExperimentV2ResponseDataType(ModelSimple):
    """
    Experiments resource type.

    :param value: If omitted defaults to "experiments". Must be one of ["experiments"].
    :type value: str
    """

    allowed_values = {
        "experiments",
    }
    EXPERIMENTS: ClassVar["ExperimentsPatchExperimentV2ResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsPatchExperimentV2ResponseDataType.EXPERIMENTS = ExperimentsPatchExperimentV2ResponseDataType("experiments")
