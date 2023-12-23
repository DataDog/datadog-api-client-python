# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class LogsCategoryProcessorType(StringEnum):
    """
    Type of logs category processor.

    :param value: If omitted defaults to "category-processor". Must be one of ["category-processor"].
    :type value: str
    """

    allowed_values = {
        "category-processor",
    }
    CATEGORY_PROCESSOR: ClassVar["LogsCategoryProcessorType"]


LogsCategoryProcessorType.CATEGORY_PROCESSOR = LogsCategoryProcessorType("category-processor")
