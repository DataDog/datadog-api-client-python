# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction(ModelSimple):
    """
    Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card).

    :param value: If omitted defaults to "partial_redact". Must be one of ["partial_redact"].
    :type value: str
    """

    allowed_values = {
        "partial_redact",
    }
    PARTIAL_REDACT: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction.PARTIAL_REDACT = (
    ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction("partial_redact")
)
