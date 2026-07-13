# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_filter_match import (
        AWSMetricNameFilterPreviewFilterMatch,
    )
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_metric import AWSMetricNameFilterPreviewMetric


class AWSMetricNameFilterPreviewNamespace(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_filter_match import (
            AWSMetricNameFilterPreviewFilterMatch,
        )
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_metric import AWSMetricNameFilterPreviewMetric

        return {
            "filters": ([AWSMetricNameFilterPreviewFilterMatch],),
            "metrics": ([AWSMetricNameFilterPreviewMetric],),
            "namespace": (str,),
        }

    attribute_map = {
        "filters": "filters",
        "metrics": "metrics",
        "namespace": "namespace",
    }

    def __init__(
        self_,
        filters: List[AWSMetricNameFilterPreviewFilterMatch],
        metrics: List[AWSMetricNameFilterPreviewMetric],
        namespace: str,
        **kwargs,
    ):
        """
        The metric name filter preview for a single namespace.

        :param filters: The metric name filter patterns evaluated for this namespace and how many metrics they matched.
        :type filters: [AWSMetricNameFilterPreviewFilterMatch]

        :param metrics: The CloudWatch metrics collected for this namespace and whether each resulting
            Datadog metric is filtered.
        :type metrics: [AWSMetricNameFilterPreviewMetric]

        :param namespace: The AWS CloudWatch namespace.
        :type namespace: str
        """
        super().__init__(kwargs)

        self_.filters = filters
        self_.metrics = metrics
        self_.namespace = namespace
