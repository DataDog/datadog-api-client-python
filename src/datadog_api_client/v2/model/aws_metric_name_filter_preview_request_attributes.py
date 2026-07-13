# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_metric_name_filters import AWSMetricNameFilters
    from datadog_api_client.v2.model.aws_metric_name_filters_include_only import AWSMetricNameFiltersIncludeOnly
    from datadog_api_client.v2.model.aws_metric_name_filters_exclude_only import AWSMetricNameFiltersExcludeOnly


class AWSMetricNameFilterPreviewRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filters import AWSMetricNameFilters

        return {
            "metric_name_filters": ([AWSMetricNameFilters],),
        }

    attribute_map = {
        "metric_name_filters": "metric_name_filters",
    }

    def __init__(
        self_,
        metric_name_filters: List[
            Union[AWSMetricNameFilters, AWSMetricNameFiltersIncludeOnly, AWSMetricNameFiltersExcludeOnly]
        ],
        **kwargs,
    ):
        """
        AWS metric name filter preview request attributes.

        :param metric_name_filters: The metric name filters to preview.
        :type metric_name_filters: [AWSMetricNameFilters]
        """
        super().__init__(kwargs)

        self_.metric_name_filters = metric_name_filters
