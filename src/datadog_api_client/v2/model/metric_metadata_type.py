# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricMetadataType(ModelSimple):
    """
    The metric metadata resource type.

    :param value: If omitted defaults to "metric_metadata". Must be one of ["metric_metadata"].
    :type value: str
    """

    allowed_values = {
        "metric_metadata",
    }
    METRIC_METADATA: ClassVar["MetricMetadataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricMetadataType.METRIC_METADATA = MetricMetadataType("metric_metadata")
