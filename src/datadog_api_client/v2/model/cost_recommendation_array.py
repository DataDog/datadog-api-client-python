# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_data import CostRecommendationData
    from datadog_api_client.v2.model.recommendations_page_meta import RecommendationsPageMeta


class CostRecommendationArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_data import CostRecommendationData
        from datadog_api_client.v2.model.recommendations_page_meta import RecommendationsPageMeta

        return {
            "data": ([CostRecommendationData],),
            "meta": (RecommendationsPageMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[CostRecommendationData], meta: Union[RecommendationsPageMeta, UnsetType] = unset, **kwargs
    ):
        """
        A page of cost recommendations with pagination metadata.

        :param data: The list of cost recommendations on this page.
        :type data: [CostRecommendationData]

        :param meta: Top-level JSON:API meta object for paginated cost recommendation responses.
        :type meta: RecommendationsPageMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
