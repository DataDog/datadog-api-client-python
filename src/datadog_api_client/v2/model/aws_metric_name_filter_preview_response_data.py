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
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_response_attributes import (
        AWSMetricNameFilterPreviewResponseAttributes,
    )
    from datadog_api_client.v2.model.aws_metric_name_filter_preview_type import AWSMetricNameFilterPreviewType


class AWSMetricNameFilterPreviewResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_response_attributes import (
            AWSMetricNameFilterPreviewResponseAttributes,
        )
        from datadog_api_client.v2.model.aws_metric_name_filter_preview_type import AWSMetricNameFilterPreviewType

        return {
            "attributes": (AWSMetricNameFilterPreviewResponseAttributes,),
            "id": (str,),
            "type": (AWSMetricNameFilterPreviewType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AWSMetricNameFilterPreviewResponseAttributes,
        id: str,
        type: AWSMetricNameFilterPreviewType,
        **kwargs,
    ):
        """
        AWS metric name filter preview response data.

        :param attributes: AWS metric name filter preview response attributes.
        :type attributes: AWSMetricNameFilterPreviewResponseAttributes

        :param id: Unique Datadog ID of the AWS Account Integration Config.
            To get the config ID for an account, use the
            `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_
            endpoint and query by AWS Account ID.
        :type id: str

        :param type: The ``AWSMetricNameFilterPreviewResponseData`` ``type``.
        :type type: AWSMetricNameFilterPreviewType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
