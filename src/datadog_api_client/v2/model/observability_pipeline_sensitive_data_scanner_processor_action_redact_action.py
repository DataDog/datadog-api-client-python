# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction(ModelSimple):
    """
    Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility.

    :param value: If omitted defaults to "redact". Must be one of ["redact"].
    :type value: str
    """

    allowed_values = {
        "redact",
    }
    REDACT: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction.REDACT = (
    ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction("redact")
)
