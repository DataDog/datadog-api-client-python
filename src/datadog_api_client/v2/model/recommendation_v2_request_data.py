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
    from datadog_api_client.v2.model.recommendation_v2_request_attributes import RecommendationV2RequestAttributes
    from datadog_api_client.v2.model.recommendation_v2_request_type import RecommendationV2RequestType


class RecommendationV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendation_v2_request_attributes import RecommendationV2RequestAttributes
        from datadog_api_client.v2.model.recommendation_v2_request_type import RecommendationV2RequestType

        return {
            "attributes": (RecommendationV2RequestAttributes,),
            "type": (RecommendationV2RequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RecommendationV2RequestAttributes, type: RecommendationV2RequestType, **kwargs):
        """
        JSON:API resource object for the SPA v2 recommendation request.

        :param attributes: Attributes for requesting SPA recommendations by forwarding a Spark job's raw arguments
            instead of a precomputed shard.
        :type attributes: RecommendationV2RequestAttributes

        :param type: JSON:API resource type for the SPA v2 recommendation request.
        :type type: RecommendationV2RequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
