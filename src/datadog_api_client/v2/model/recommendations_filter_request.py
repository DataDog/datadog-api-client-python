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
    from datadog_api_client.v2.model.recommendations_filter_request_data import RecommendationsFilterRequestData


class RecommendationsFilterRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendations_filter_request_data import RecommendationsFilterRequestData

        return {
            "data": (RecommendationsFilterRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RecommendationsFilterRequestData, **kwargs):
        """
        JSON:API request body for filtering cost recommendations.

        :param data: JSON:API resource containing the cost recommendations filter. This legacy search contract
            uses the resource ID for the filter expression rather than as a persistent resource identifier.
        :type data: RecommendationsFilterRequestData
        """
        super().__init__(kwargs)

        self_.data = data
