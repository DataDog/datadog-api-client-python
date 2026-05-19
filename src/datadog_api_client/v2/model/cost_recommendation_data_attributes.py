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
    from datadog_api_client.v2.model.cost_recommendation_data_attributes_potential_daily_savings import (
        CostRecommendationDataAttributesPotentialDailySavings,
    )


class CostRecommendationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_data_attributes_potential_daily_savings import (
            CostRecommendationDataAttributesPotentialDailySavings,
        )

        return {
            "dd_resource_key": (str,),
            "potential_daily_savings": (CostRecommendationDataAttributesPotentialDailySavings,),
            "recommendation_type": (str,),
            "resource_id": (str,),
            "resource_type": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "dd_resource_key": "dd_resource_key",
        "potential_daily_savings": "potential_daily_savings",
        "recommendation_type": "recommendation_type",
        "resource_id": "resource_id",
        "resource_type": "resource_type",
        "tags": "tags",
    }

    def __init__(
        self_,
        dd_resource_key: Union[str, UnsetType] = unset,
        potential_daily_savings: Union[CostRecommendationDataAttributesPotentialDailySavings, UnsetType] = unset,
        recommendation_type: Union[str, UnsetType] = unset,
        resource_id: Union[str, UnsetType] = unset,
        resource_type: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes describing a single cost recommendation.

        :param dd_resource_key: Datadog resource key identifying the recommended resource.
        :type dd_resource_key: str, optional

        :param potential_daily_savings: Estimated daily savings if the recommendation is applied.
        :type potential_daily_savings: CostRecommendationDataAttributesPotentialDailySavings, optional

        :param recommendation_type: The kind of recommendation (for example, ``terminate`` or ``rightsize`` ).
        :type recommendation_type: str, optional

        :param resource_id: Cloud provider identifier of the resource.
        :type resource_id: str, optional

        :param resource_type: Resource type (for example, ``aws_ec2_instance`` ).
        :type resource_type: str, optional

        :param tags: Tags attached to the recommended resource.
        :type tags: [str], optional
        """
        if dd_resource_key is not unset:
            kwargs["dd_resource_key"] = dd_resource_key
        if potential_daily_savings is not unset:
            kwargs["potential_daily_savings"] = potential_daily_savings
        if recommendation_type is not unset:
            kwargs["recommendation_type"] = recommendation_type
        if resource_id is not unset:
            kwargs["resource_id"] = resource_id
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
