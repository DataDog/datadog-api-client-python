# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsSearchSpansRequestType(ModelSimple):
    """
    Resource type for an LLM Observability spans search request.

    :param value: If omitted defaults to "spans". Must be one of ["spans"].
    :type value: str
    """

    allowed_values = {
        "spans",
    }
    SPANS: ClassVar["LLMObsSearchSpansRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsSearchSpansRequestType.SPANS = LLMObsSearchSpansRequestType("spans")
