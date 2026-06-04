# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnnotationsType(ModelSimple):
    """
    Resource type for LLM Observability annotations.

    :param value: If omitted defaults to "annotations". Must be one of ["annotations"].
    :type value: str
    """

    allowed_values = {
        "annotations",
    }
    ANNOTATIONS: ClassVar["LLMObsAnnotationsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnnotationsType.ANNOTATIONS = LLMObsAnnotationsType("annotations")
