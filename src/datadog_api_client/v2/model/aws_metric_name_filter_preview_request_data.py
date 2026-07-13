# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_request_attributes import (
        AWSMetricNameFilterPreviewRequestAttributes,
    )
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_type import AWSMetricNameFilterPreviewType


class AWSMetricNameFilterPreviewRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_request_attributes import (
            AWSMetricNameFilterPreviewRequestAttributes,
        )
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_type import AWSMetricNameFilterPreviewType

        return {
            "attributes": (AWSMetricNameFilterPreviewRequestAttributes,),
            "type": (AWSMetricNameFilterPreviewType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AWSMetricNameFilterPreviewRequestAttributes, type: AWSMetricNameFilterPreviewType, **kwargs
    ):
        """
        AWS metric name filter preview request data.

        :param attributes: AWS metric name filter preview request attributes.
        :type attributes: AWSMetricNameFilterPreviewRequestAttributes

        :param type: The ``AWSMetricNameFilterPreviewResponseData`` ``type``.
        :type type: AWSMetricNameFilterPreviewType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
