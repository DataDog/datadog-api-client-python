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
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_dd_name import AWSMetricNameFilterPreviewDDName


class AWSMetricNameFilterPreviewMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_dd_name import AWSMetricNameFilterPreviewDDName

        return {
            "cw_name": (str,),
            "dd_names": ([AWSMetricNameFilterPreviewDDName],),
        }

    attribute_map = {
        "cw_name": "cw_name",
        "dd_names": "dd_names",
    }

    def __init__(self_, cw_name: str, dd_names: List[AWSMetricNameFilterPreviewDDName], **kwargs):
        """
        A CloudWatch metric and the Datadog metric names it produces.

        :param cw_name: The CloudWatch metric name.
        :type cw_name: str

        :param dd_names: The Datadog metric names produced from this CloudWatch metric.
        :type dd_names: [AWSMetricNameFilterPreviewDDName]
        """
        super().__init__(kwargs)

        self_.cw_name = cw_name
        self_.dd_names = dd_names
