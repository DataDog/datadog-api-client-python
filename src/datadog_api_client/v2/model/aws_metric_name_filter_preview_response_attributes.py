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
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_namespace import AWSMetricNameFilterPreviewNamespace


class AWSMetricNameFilterPreviewResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_namespace import (
            AWSMetricNameFilterPreviewNamespace,
        )

        return {
            "namespaces": ([AWSMetricNameFilterPreviewNamespace],),
        }

    attribute_map = {
        "namespaces": "namespaces",
    }

    def __init__(self_, namespaces: List[AWSMetricNameFilterPreviewNamespace], **kwargs):
        """
        AWS metric name filter preview response attributes.

        :param namespaces: The list of namespaces affected by the previewed metric name filters.
        :type namespaces: [AWSMetricNameFilterPreviewNamespace]
        """
        super().__init__(kwargs)

        self_.namespaces = namespaces
