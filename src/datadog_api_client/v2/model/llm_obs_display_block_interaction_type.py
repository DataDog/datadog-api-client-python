# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsDisplayBlockInteractionType(ModelSimple):
    """
    Type discriminator for a `display_block` interaction.

    :param value: If omitted defaults to "display_block". Must be one of ["display_block"].
    :type value: str
    """

    allowed_values = {
        "display_block",
    }
    DISPLAY_BLOCK: ClassVar["LLMObsDisplayBlockInteractionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsDisplayBlockInteractionType.DISPLAY_BLOCK = LLMObsDisplayBlockInteractionType("display_block")
