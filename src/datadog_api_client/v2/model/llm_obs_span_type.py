# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsSpanType(ModelSimple):
    """
    Resource type for an LLM Observability span.

    :param value: If omitted defaults to "span". Must be one of ["span"].
    :type value: str
    """

    allowed_values = {
        "span",
    }
    SPAN: ClassVar["LLMObsSpanType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsSpanType.SPAN = LLMObsSpanType("span")
