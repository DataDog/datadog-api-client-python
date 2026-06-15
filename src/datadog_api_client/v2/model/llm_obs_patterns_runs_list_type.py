# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsRunsListType(ModelSimple):
    """
    Resource type of a list of LLM Observability patterns runs.

    :param value: If omitted defaults to "list_topic_discovery_runs_response". Must be one of ["list_topic_discovery_runs_response"].
    :type value: str
    """

    allowed_values = {
        "list_topic_discovery_runs_response",
    }
    LIST_TOPIC_DISCOVERY_RUNS_RESPONSE: ClassVar["LLMObsPatternsRunsListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsRunsListType.LIST_TOPIC_DISCOVERY_RUNS_RESPONSE = LLMObsPatternsRunsListType(
    "list_topic_discovery_runs_response"
)
