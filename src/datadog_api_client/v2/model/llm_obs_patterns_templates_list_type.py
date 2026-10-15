# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsTemplatesListType(ModelSimple):
    """
    Resource type of a list of Agent Observability patterns templates.

    :param value: If omitted defaults to "list_topic_discovery_templates_response". Must be one of ["list_topic_discovery_templates_response"].
    :type value: str
    """

    allowed_values = {
        "list_topic_discovery_templates_response",
    }
    LIST_TOPIC_DISCOVERY_TEMPLATES_RESPONSE: ClassVar["LLMObsPatternsTemplatesListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsTemplatesListType.LIST_TOPIC_DISCOVERY_TEMPLATES_RESPONSE = LLMObsPatternsTemplatesListType(
    "list_topic_discovery_templates_response"
)
