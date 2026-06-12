# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsRequestType(ModelSimple):
    """
    Resource type for triggering an LLM Observability patterns run.

    :param value: If omitted defaults to "topic_discovery". Must be one of ["topic_discovery"].
    :type value: str
    """

    allowed_values = {
        "topic_discovery",
    }
    TOPIC_DISCOVERY: ClassVar["LLMObsPatternsRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsRequestType.TOPIC_DISCOVERY = LLMObsPatternsRequestType("topic_discovery")
