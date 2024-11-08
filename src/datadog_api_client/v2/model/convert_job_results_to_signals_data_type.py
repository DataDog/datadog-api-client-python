# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ConvertJobResultsToSignalsDataType(ModelSimple):
    """
    Type of payload.

    :param value: If omitted defaults to "historicalDetectionsJobResultSignalConversion". Must be one of ["historicalDetectionsJobResultSignalConversion"].
    :type value: str
    """

    allowed_values = {
        "historicalDetectionsJobResultSignalConversion",
    }
    HISTORICALDETECTIONSJOBRESULTSIGNALCONVERSION: ClassVar["ConvertJobResultsToSignalsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ConvertJobResultsToSignalsDataType.HISTORICALDETECTIONSJOBRESULTSIGNALCONVERSION = ConvertJobResultsToSignalsDataType(
    "historicalDetectionsJobResultSignalConversion"
)
