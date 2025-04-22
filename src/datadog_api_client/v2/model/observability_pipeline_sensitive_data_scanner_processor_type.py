# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorType(ModelSimple):
    """
    The processor type. The value should always be `sensitive_data_scanner`.

    :param value: If omitted defaults to "sensitive_data_scanner". Must be one of ["sensitive_data_scanner"].
    :type value: str
    """

    allowed_values = {
        "sensitive_data_scanner",
    }
    SENSITIVE_DATA_SCANNER: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorType.SENSITIVE_DATA_SCANNER = (
    ObservabilityPipelineSensitiveDataScannerProcessorType("sensitive_data_scanner")
)
