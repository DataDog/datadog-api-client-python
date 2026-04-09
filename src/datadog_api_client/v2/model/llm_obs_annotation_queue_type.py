# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnnotationQueueType(ModelSimple):
    """
    Resource type of an LLM Observability annotation queue.

    :param value: If omitted defaults to "queues". Must be one of ["queues"].
    :type value: str
    """

    allowed_values = {
        "queues",
    }
    QUEUES: ClassVar["LLMObsAnnotationQueueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnnotationQueueType.QUEUES = LLMObsAnnotationQueueType("queues")
