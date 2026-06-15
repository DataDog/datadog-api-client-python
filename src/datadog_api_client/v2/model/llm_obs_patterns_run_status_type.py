# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsRunStatusType(ModelSimple):
    """
    Resource type of an LLM Observability patterns run status.

    :param value: If omitted defaults to "topic_discovery_run_status". Must be one of ["topic_discovery_run_status"].
    :type value: str
    """

    allowed_values = {
        "topic_discovery_run_status",
    }
    TOPIC_DISCOVERY_RUN_STATUS: ClassVar["LLMObsPatternsRunStatusType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsRunStatusType.TOPIC_DISCOVERY_RUN_STATUS = LLMObsPatternsRunStatusType("topic_discovery_run_status")
