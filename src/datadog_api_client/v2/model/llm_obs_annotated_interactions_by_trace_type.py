# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnnotatedInteractionsByTraceType(ModelSimple):
    """
    Resource type for cross-queue annotated interactions lookup.

    :param value: If omitted defaults to "annotated_interactions_by_trace". Must be one of ["annotated_interactions_by_trace"].
    :type value: str
    """

    allowed_values = {
        "annotated_interactions_by_trace",
    }
    ANNOTATED_INTERACTIONS_BY_TRACE: ClassVar["LLMObsAnnotatedInteractionsByTraceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnnotatedInteractionsByTraceType.ANNOTATED_INTERACTIONS_BY_TRACE = LLMObsAnnotatedInteractionsByTraceType(
    "annotated_interactions_by_trace"
)
