# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionFilterType(ModelSimple):
    """
    The type of retention filter. The value should always be spans-sampling-processor.

    :param value: If omitted defaults to "spans-sampling-processor". Must be one of ["spans-sampling-processor"].
    :type value: str
    """

    allowed_values = {
        "spans-sampling-processor",
    }
    SPANS_SAMPLING_PROCESSOR: ClassVar["RetentionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionFilterType.SPANS_SAMPLING_PROCESSOR = RetentionFilterType("spans-sampling-processor")
