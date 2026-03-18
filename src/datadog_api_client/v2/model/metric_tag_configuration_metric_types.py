# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricTagConfigurationMetricTypes(ModelSimple):
    """
    The metric's type. Contact your Customer Success Manager (CSM) for instructions on how to use the histogram types.

    :param value: If omitted defaults to "gauge". Must be one of ["gauge", "count", "rate", "distribution", "exponential_histogram", "explicit_histogram"].
    :type value: str
    """

    allowed_values = {
        "gauge",
        "count",
        "rate",
        "distribution",
        "exponential_histogram",
        "explicit_histogram",
    }
    GAUGE: ClassVar["MetricTagConfigurationMetricTypes"]
    COUNT: ClassVar["MetricTagConfigurationMetricTypes"]
    RATE: ClassVar["MetricTagConfigurationMetricTypes"]
    DISTRIBUTION: ClassVar["MetricTagConfigurationMetricTypes"]
    EXPONENTIAL_HISTOGRAM: ClassVar["MetricTagConfigurationMetricTypes"]
    EXPLICIT_HISTOGRAM: ClassVar["MetricTagConfigurationMetricTypes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricTagConfigurationMetricTypes.GAUGE = MetricTagConfigurationMetricTypes("gauge")
MetricTagConfigurationMetricTypes.COUNT = MetricTagConfigurationMetricTypes("count")
MetricTagConfigurationMetricTypes.RATE = MetricTagConfigurationMetricTypes("rate")
MetricTagConfigurationMetricTypes.DISTRIBUTION = MetricTagConfigurationMetricTypes("distribution")
MetricTagConfigurationMetricTypes.EXPONENTIAL_HISTOGRAM = MetricTagConfigurationMetricTypes("exponential_histogram")
MetricTagConfigurationMetricTypes.EXPLICIT_HISTOGRAM = MetricTagConfigurationMetricTypes("explicit_histogram")
