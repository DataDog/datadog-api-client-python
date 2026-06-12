# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGenerateMetricsV2ProcessorType(ModelSimple):
    """
    The processor type. Always `generate_metrics`.

    :param value: If omitted defaults to "generate_metrics". Must be one of ["generate_metrics"].
    :type value: str
    """

    allowed_values = {
        "generate_metrics",
    }
    GENERATE_METRICS: ClassVar["ObservabilityPipelineGenerateMetricsV2ProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGenerateMetricsV2ProcessorType.GENERATE_METRICS = (
    ObservabilityPipelineGenerateMetricsV2ProcessorType("generate_metrics")
)
