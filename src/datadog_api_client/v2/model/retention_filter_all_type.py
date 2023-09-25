# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionFilterAllType(ModelSimple):
    """
    The type of retention filter.

    :param value: If omitted defaults to "spans-sampling-processor". Must be one of ["spans-sampling-processor", "spans-errors-sampling-processor", "spans-appsec-sampling-processor"].
    :type value: str
    """

    allowed_values = {
        "spans-sampling-processor",
        "spans-errors-sampling-processor",
        "spans-appsec-sampling-processor",
    }
    SPANS_SAMPLING_PROCESSOR: ClassVar["RetentionFilterAllType"]
    SPANS_ERRORS_SAMPLING_PROCESSOR: ClassVar["RetentionFilterAllType"]
    SPANS_APPSEC_SAMPLING_PROCESSOR: ClassVar["RetentionFilterAllType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionFilterAllType.SPANS_SAMPLING_PROCESSOR = RetentionFilterAllType("spans-sampling-processor")
RetentionFilterAllType.SPANS_ERRORS_SAMPLING_PROCESSOR = RetentionFilterAllType("spans-errors-sampling-processor")
RetentionFilterAllType.SPANS_APPSEC_SAMPLING_PROCESSOR = RetentionFilterAllType("spans-appsec-sampling-processor")
