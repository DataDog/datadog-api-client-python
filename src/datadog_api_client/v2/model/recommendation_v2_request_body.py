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
    from datadog_api_client.v2.model.recommendation_v2_request_data import RecommendationV2RequestData


class RecommendationV2RequestBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendation_v2_request_data import RecommendationV2RequestData

        return {
            "data": (RecommendationV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RecommendationV2RequestData, **kwargs):
        """
        Request body for retrieving SPA recommendations by forwarding a Spark job's raw arguments
        instead of a precomputed shard.

        :param data: JSON:API resource object for the SPA v2 recommendation request.
        :type data: RecommendationV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
