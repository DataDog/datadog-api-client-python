# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineMetricTagsProcessorType(ModelSimple):
    """
    The processor type. The value should always be `metric_tags`.

    :param value: If omitted defaults to "metric_tags". Must be one of ["metric_tags"].
    :type value: str
    """

    allowed_values = {
        "metric_tags",
    }
    METRIC_TAGS: ClassVar["ObservabilityPipelineMetricTagsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineMetricTagsProcessorType.METRIC_TAGS = ObservabilityPipelineMetricTagsProcessorType("metric_tags")
