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
    from datadog_api_client.v2.model.metric_metadata_data import MetricMetadataData


class MetricMetadataListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_metadata_data import MetricMetadataData

        return {
            "data": ([MetricMetadataData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[MetricMetadataData], **kwargs):
        """
        Metadata for each requested metric that exists, in request order.

        :param data: One item per requested metric that exists. Metrics that don't exist are left out.
        :type data: [MetricMetadataData]
        """
        super().__init__(kwargs)

        self_.data = data
