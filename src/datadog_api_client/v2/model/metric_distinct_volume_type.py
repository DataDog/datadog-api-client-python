# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class MetricDistinctVolumeType(StringEnum):
    """
    The metric distinct volume type.

    :param value: If omitted defaults to "distinct_metric_volumes". Must be one of ["distinct_metric_volumes"].
    :type value: str
    """

    allowed_values = {
        "distinct_metric_volumes",
    }
    DISTINCT_METRIC_VOLUMES: ClassVar["MetricDistinctVolumeType"]


MetricDistinctVolumeType.DISTINCT_METRIC_VOLUMES = MetricDistinctVolumeType("distinct_metric_volumes")
