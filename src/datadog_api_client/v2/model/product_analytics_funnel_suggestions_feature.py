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
    from datadog_api_client.v2.model.product_analytics_core_user_journey import ProductAnalyticsCoreUserJourney


class ProductAnalyticsFunnelSuggestionsFeature(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_core_user_journey import ProductAnalyticsCoreUserJourney

        return {
            "core_user_journeys": ([ProductAnalyticsCoreUserJourney],),
            "description": (str,),
            "id": (str,),
            "name": (str,),
            "score": (int,),
            "support": (int,),
        }

    attribute_map = {
        "core_user_journeys": "core_user_journeys",
        "description": "description",
        "id": "id",
        "name": "name",
        "score": "score",
        "support": "support",
    }

    def __init__(
        self_,
        core_user_journeys: Union[List[ProductAnalyticsCoreUserJourney], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        score: Union[int, UnsetType] = unset,
        support: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A feature detected in the application, with the journeys users take to use it.

        :param core_user_journeys: The suggested journey that users follow to use the feature. Contains one journey.
        :type core_user_journeys: [ProductAnalyticsCoreUserJourney], optional

        :param description: Description of the feature.
        :type description: str, optional

        :param id: ID of the feature.
        :type id: str, optional

        :param name: Name of the feature.
        :type name: str, optional

        :param score: Relevance score of the feature. Higher is more relevant.
        :type score: int, optional

        :param support: Number of sessions that used the feature.
        :type support: int, optional
        """
        if core_user_journeys is not unset:
            kwargs["core_user_journeys"] = core_user_journeys
        if description is not unset:
            kwargs["description"] = description
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if score is not unset:
            kwargs["score"] = score
        if support is not unset:
            kwargs["support"] = support
        super().__init__(kwargs)
