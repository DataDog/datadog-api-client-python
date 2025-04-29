# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection(ModelSimple):
    """
    Indicates whether to redact characters from the first or last part of the matched value.

    :param value: Must be one of ["first", "last"].
    :type value: str
    """

    allowed_values = {
        "first",
        "last",
    }
    FIRST: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection"]
    LAST: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection.FIRST = (
    ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection("first")
)
ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection.LAST = (
    ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection("last")
)
