# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineRenameMetricTagsProcessorType(ModelSimple):
    """
    The processor type. The value must be `rename_metric_tags`.

    :param value: If omitted defaults to "rename_metric_tags". Must be one of ["rename_metric_tags"].
    :type value: str
    """

    allowed_values = {
        "rename_metric_tags",
    }
    RENAME_METRIC_TAGS: ClassVar["ObservabilityPipelineRenameMetricTagsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineRenameMetricTagsProcessorType.RENAME_METRIC_TAGS = (
    ObservabilityPipelineRenameMetricTagsProcessorType("rename_metric_tags")
)
