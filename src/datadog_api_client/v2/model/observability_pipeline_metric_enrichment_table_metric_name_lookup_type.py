# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType(ModelSimple):
    """
    The lookup source type. The value should always be `metric_name`.

    :param value: If omitted defaults to "metric_name". Must be one of ["metric_name"].
    :type value: str
    """

    allowed_values = {
        "metric_name",
    }
    METRIC_NAME: ClassVar["ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType.METRIC_NAME = (
    ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType("metric_name")
)
