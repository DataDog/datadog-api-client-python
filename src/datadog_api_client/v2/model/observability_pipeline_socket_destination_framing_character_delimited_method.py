# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod(ModelSimple):
    """
    The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object.

    :param value: If omitted defaults to "character_delimited". Must be one of ["character_delimited"].
    :type value: str
    """

    allowed_values = {
        "character_delimited",
    }
    CHARACTER_DELIMITED: ClassVar["ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod.CHARACTER_DELIMITED = (
    ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod("character_delimited")
)
