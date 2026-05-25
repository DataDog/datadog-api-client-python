# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnalysisRequestDataType(ModelSimple):
    """
    Analysis request resource type.

    :param value: If omitted defaults to "analysis_request". Must be one of ["analysis_request"].
    :type value: str
    """

    allowed_values = {
        "analysis_request",
    }
    ANALYSIS_REQUEST: ClassVar["AnalysisRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnalysisRequestDataType.ANALYSIS_REQUEST = AnalysisRequestDataType("analysis_request")
