# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode(ModelSimple):
    """
    Whether exposure uses a fixed fraction or a sequence of steps.

    :param value: Must be one of ["STATIC", "STEPS"].
    :type value: str
    """

    allowed_values = {
        "STATIC",
        "STEPS",
    }
    STATIC: ClassVar["ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode"]
    STEPS: ClassVar["ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode.STATIC = (
    ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode("STATIC")
)
ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode.STEPS = (
    ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode("STEPS")
)
