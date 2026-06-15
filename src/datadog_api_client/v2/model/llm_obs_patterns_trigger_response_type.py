# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsTriggerResponseType(ModelSimple):
    """
    Resource type of an LLM Observability patterns trigger response.

    :param value: If omitted defaults to "topic_discovery_run". Must be one of ["topic_discovery_run"].
    :type value: str
    """

    allowed_values = {
        "topic_discovery_run",
    }
    TOPIC_DISCOVERY_RUN: ClassVar["LLMObsPatternsTriggerResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsTriggerResponseType.TOPIC_DISCOVERY_RUN = LLMObsPatternsTriggerResponseType("topic_discovery_run")
