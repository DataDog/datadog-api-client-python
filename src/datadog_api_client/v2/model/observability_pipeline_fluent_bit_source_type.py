# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineFluentBitSourceType(ModelSimple):
    """
    The source type. The value should always be `fluent_bit`.

    :param value: If omitted defaults to "fluent_bit". Must be one of ["fluent_bit"].
    :type value: str
    """

    allowed_values = {
        "fluent_bit",
    }
    FLUENT_BIT: ClassVar["ObservabilityPipelineFluentBitSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineFluentBitSourceType.FLUENT_BIT = ObservabilityPipelineFluentBitSourceType("fluent_bit")
