# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsEventType(ModelSimple):
    """
    Resource type for LLM Observability experiment events.

    :param value: If omitted defaults to "events". Must be one of ["events"].
    :type value: str
    """

    allowed_values = {
        "events",
    }
    EVENTS: ClassVar["LLMObsEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsEventType.EVENTS = LLMObsEventType("events")
