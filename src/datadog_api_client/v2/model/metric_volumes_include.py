# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricVolumesInclude(ModelSimple):
    """
    Comma-separated list of additional data to include in the response. Allowed values are `metric_volumes`.

    :param value: Must be one of ["metric_volumes", "generated_metric_attributes"].
    :type value: str
    """

    allowed_values = {
        "metric_volumes",
        "generated_metric_attributes",
    }
    METRIC_VOLUMES: ClassVar["MetricVolumesInclude"]
    GENERATED_METRIC_ATTRIBUTES: ClassVar["MetricVolumesInclude"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricVolumesInclude.METRIC_VOLUMES = MetricVolumesInclude("metric_volumes")
MetricVolumesInclude.GENERATED_METRIC_ATTRIBUTES = MetricVolumesInclude("generated_metric_attributes")
