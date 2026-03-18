# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableMetricsQueryDataSource(ModelSimple):
    """
    Metrics data source.

    :param value: Must be one of ["metrics", "cloud_cost"].
    :type value: str
    """

    allowed_values = {
        "metrics",
        "cloud_cost",
    }
    METRICS: ClassVar["GuidedTableMetricsQueryDataSource"]
    CLOUD_COST: ClassVar["GuidedTableMetricsQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableMetricsQueryDataSource.METRICS = GuidedTableMetricsQueryDataSource("metrics")
GuidedTableMetricsQueryDataSource.CLOUD_COST = GuidedTableMetricsQueryDataSource("cloud_cost")
