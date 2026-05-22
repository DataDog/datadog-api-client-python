# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAddMetricTagsProcessorType(ModelSimple):
    """
    The processor type. The value must be `add_metric_tags`.

    :param value: If omitted defaults to "add_metric_tags". Must be one of ["add_metric_tags"].
    :type value: str
    """

    allowed_values = {
        "add_metric_tags",
    }
    ADD_METRIC_TAGS: ClassVar["ObservabilityPipelineAddMetricTagsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAddMetricTagsProcessorType.ADD_METRIC_TAGS = ObservabilityPipelineAddMetricTagsProcessorType(
    "add_metric_tags"
)
