# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSMetricNameFilterPreviewType(ModelSimple):
    """
    The `AWSMetricNameFilterPreviewResponseData` `type`.

    :param value: If omitted defaults to "metric_name_filter_preview". Must be one of ["metric_name_filter_preview"].
    :type value: str
    """

    allowed_values = {
        "metric_name_filter_preview",
    }
    METRIC_NAME_FILTER_PREVIEW: ClassVar["AWSMetricNameFilterPreviewType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSMetricNameFilterPreviewType.METRIC_NAME_FILTER_PREVIEW = AWSMetricNameFilterPreviewType("metric_name_filter_preview")
