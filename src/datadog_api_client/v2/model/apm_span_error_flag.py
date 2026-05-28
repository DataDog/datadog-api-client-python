# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class APMSpanErrorFlag(ModelSimple):
    """
    Error flag for a span. `1` when the span is in error, `0` otherwise.

    :param value: Must be one of [0, 1].
    :type value: int
    """

    allowed_values = {
        0,
        1,
    }
    NO_ERROR: ClassVar["APMSpanErrorFlag"]
    ERROR: ClassVar["APMSpanErrorFlag"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


APMSpanErrorFlag.NO_ERROR = APMSpanErrorFlag(0)
APMSpanErrorFlag.ERROR = APMSpanErrorFlag(1)
