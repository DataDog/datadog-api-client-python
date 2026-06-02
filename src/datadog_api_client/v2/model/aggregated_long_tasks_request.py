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
    from datadog_api_client.v2.model.aggregated_long_tasks_request_data import AggregatedLongTasksRequestData


class AggregatedLongTasksRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_long_tasks_request_data import AggregatedLongTasksRequestData

        return {
            "data": (AggregatedLongTasksRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AggregatedLongTasksRequestData, **kwargs):
        """
        Request body for the aggregated long tasks endpoint.

        :param data: Data envelope for an aggregated long tasks request.
        :type data: AggregatedLongTasksRequestData
        """
        super().__init__(kwargs)

        self_.data = data
