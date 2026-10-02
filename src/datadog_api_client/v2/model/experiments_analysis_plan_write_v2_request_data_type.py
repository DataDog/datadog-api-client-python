# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsAnalysisPlanWriteV2RequestDataType(ModelSimple):
    """
    Analysis plans resource type.

    :param value: If omitted defaults to "analysis-plans". Must be one of ["analysis-plans"].
    :type value: str
    """

    allowed_values = {
        "analysis-plans",
    }
    ANALYSIS_PLANS: ClassVar["ExperimentsAnalysisPlanWriteV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsAnalysisPlanWriteV2RequestDataType.ANALYSIS_PLANS = ExperimentsAnalysisPlanWriteV2RequestDataType(
    "analysis-plans"
)
