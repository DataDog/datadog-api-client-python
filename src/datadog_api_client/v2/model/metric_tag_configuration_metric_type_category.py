# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricTagConfigurationMetricTypeCategory(ModelSimple):
    """
    The metric's type category.

    :param value: If omitted defaults to "distribution". Must be one of ["non_distribution", "distribution", "exponential_histogram", "explicit_histogram"].
    :type value: str
    """

    allowed_values = {
        "non_distribution",
        "distribution",
        "exponential_histogram",
        "explicit_histogram",
    }
    NON_DISTRIBUTION: ClassVar["MetricTagConfigurationMetricTypeCategory"]
    DISTRIBUTION: ClassVar["MetricTagConfigurationMetricTypeCategory"]
    EXPONENTIAL_HISTOGRAM: ClassVar["MetricTagConfigurationMetricTypeCategory"]
    EXPLICIT_HISTOGRAM: ClassVar["MetricTagConfigurationMetricTypeCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricTagConfigurationMetricTypeCategory.NON_DISTRIBUTION = MetricTagConfigurationMetricTypeCategory("non_distribution")
MetricTagConfigurationMetricTypeCategory.DISTRIBUTION = MetricTagConfigurationMetricTypeCategory("distribution")
MetricTagConfigurationMetricTypeCategory.EXPONENTIAL_HISTOGRAM = MetricTagConfigurationMetricTypeCategory(
    "exponential_histogram"
)
MetricTagConfigurationMetricTypeCategory.EXPLICIT_HISTOGRAM = MetricTagConfigurationMetricTypeCategory(
    "explicit_histogram"
)
