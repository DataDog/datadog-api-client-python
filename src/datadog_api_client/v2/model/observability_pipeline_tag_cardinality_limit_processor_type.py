# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineTagCardinalityLimitProcessorType(ModelSimple):
    """
    The processor type. The value must be `tag_cardinality_limit`.

    :param value: If omitted defaults to "tag_cardinality_limit". Must be one of ["tag_cardinality_limit"].
    :type value: str
    """

    allowed_values = {
        "tag_cardinality_limit",
    }
    TAG_CARDINALITY_LIMIT: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineTagCardinalityLimitProcessorType.TAG_CARDINALITY_LIMIT = (
    ObservabilityPipelineTagCardinalityLimitProcessorType("tag_cardinality_limit")
)
