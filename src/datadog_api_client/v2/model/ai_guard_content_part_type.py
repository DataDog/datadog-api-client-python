# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIGuardContentPartType(ModelSimple):
    """
    The type of the content part.

    :param value: Must be one of ["text", "image_url"].
    :type value: str
    """

    allowed_values = {
        "text",
        "image_url",
    }
    TEXT: ClassVar["AIGuardContentPartType"]
    IMAGE_URL: ClassVar["AIGuardContentPartType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIGuardContentPartType.TEXT = AIGuardContentPartType("text")
AIGuardContentPartType.IMAGE_URL = AIGuardContentPartType("image_url")
