# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsArrayProcessorType(ModelSimple):
    """
    Type of logs array processor.

    :param value: If omitted defaults to "array-processor". Must be one of ["array-processor"].
    :type value: str
    """

    allowed_values = {
        "array-processor",
    }
    ARRAY_PROCESSOR: ClassVar["LogsArrayProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsArrayProcessorType.ARRAY_PROCESSOR = LogsArrayProcessorType("array-processor")
