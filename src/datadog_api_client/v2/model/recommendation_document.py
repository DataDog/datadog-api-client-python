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
    from datadog_api_client.v2.model.recommendation_data import RecommendationData


class RecommendationDocument(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendation_data import RecommendationData

        return {
            "data": (RecommendationData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RecommendationData, **kwargs):
        """
        JSON:API document containing a single Recommendation resource. Returned by SPA when the Spark Gateway requests recommendations.

        :param data: JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.
        :type data: RecommendationData
        """
        super().__init__(kwargs)

        self_.data = data
