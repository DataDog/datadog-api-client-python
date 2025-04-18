# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGenerateMetricsProcessorType(ModelSimple):
    """
    The processor type. Always `generate_datadog_metrics`.

    :param value: If omitted defaults to "generate_datadog_metrics". Must be one of ["generate_datadog_metrics"].
    :type value: str
    """

    allowed_values = {
        "generate_datadog_metrics",
    }
    GENERATE_DATADOG_METRICS: ClassVar["ObservabilityPipelineGenerateMetricsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGenerateMetricsProcessorType.GENERATE_DATADOG_METRICS = (
    ObservabilityPipelineGenerateMetricsProcessorType("generate_datadog_metrics")
)
