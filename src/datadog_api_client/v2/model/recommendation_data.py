# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.recommendation_attributes import RecommendationAttributes
    from datadog_api_client.v2.model.recommendation_type import RecommendationType


class RecommendationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendation_attributes import RecommendationAttributes
        from datadog_api_client.v2.model.recommendation_type import RecommendationType

        return {
            "attributes": (RecommendationAttributes,),
            "id": (str,),
            "type": (RecommendationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RecommendationAttributes,
        type: RecommendationType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.

        :param attributes: Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.
        :type attributes: RecommendationAttributes

        :param id: Resource identifier for the recommendation. Optional in responses.
        :type id: str, optional

        :param type: JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA.
        :type type: RecommendationType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
