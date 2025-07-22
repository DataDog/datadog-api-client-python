# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GreyNoiseIntegrationType(ModelSimple):
    """
    The definition of the `GreyNoiseIntegrationType` object.

    :param value: If omitted defaults to "GreyNoise". Must be one of ["GreyNoise"].
    :type value: str
    """

    allowed_values = {
        "GreyNoise",
    }
    GREYNOISE: ClassVar["GreyNoiseIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GreyNoiseIntegrationType.GREYNOISE = GreyNoiseIntegrationType("GreyNoise")
