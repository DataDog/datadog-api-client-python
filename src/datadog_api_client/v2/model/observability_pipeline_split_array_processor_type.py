# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplitArrayProcessorType(ModelSimple):
    """
    The processor type. The value should always be `split_array`.

    :param value: If omitted defaults to "split_array". Must be one of ["split_array"].
    :type value: str
    """

    allowed_values = {
        "split_array",
    }
    SPLIT_ARRAY: ClassVar["ObservabilityPipelineSplitArrayProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplitArrayProcessorType.SPLIT_ARRAY = ObservabilityPipelineSplitArrayProcessorType("split_array")
