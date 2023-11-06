# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SensitiveDataScannerStandardPatternType(StringEnum):
    """
    Sensitive Data Scanner standard pattern type.

    :param value: If omitted defaults to "sensitive_data_scanner_standard_pattern". Must be one of ["sensitive_data_scanner_standard_pattern"].
    :type value: str
    """

    allowed_values = {
        "sensitive_data_scanner_standard_pattern",
    }
    SENSITIVE_DATA_SCANNER_STANDARD_PATTERN: ClassVar["SensitiveDataScannerStandardPatternType"]


SensitiveDataScannerStandardPatternType.SENSITIVE_DATA_SCANNER_STANDARD_PATTERN = (
    SensitiveDataScannerStandardPatternType("sensitive_data_scanner_standard_pattern")
)
