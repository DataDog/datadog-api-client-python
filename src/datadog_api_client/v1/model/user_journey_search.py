# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.user_journey_search_filters import UserJourneySearchFilters
    from datadog_api_client.v1.model.user_journey_join_keys import UserJourneyJoinKeys
    from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery


class UserJourneySearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.user_journey_search_filters import UserJourneySearchFilters
        from datadog_api_client.v1.model.user_journey_join_keys import UserJourneyJoinKeys
        from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery

        return {
            "expression": (str,),
            "filters": (UserJourneySearchFilters,),
            "join_keys": (UserJourneyJoinKeys,),
            "node_objects": ({str: (ProductAnalyticsBaseQuery,)},),
            "step_aliases": ({str: (str,)},),
        }

    attribute_map = {
        "expression": "expression",
        "filters": "filters",
        "join_keys": "join_keys",
        "node_objects": "node_objects",
        "step_aliases": "step_aliases",
    }

    def __init__(
        self_,
        expression: str,
        node_objects: Dict[str, ProductAnalyticsBaseQuery],
        filters: Union[UserJourneySearchFilters, UnsetType] = unset,
        join_keys: Union[UserJourneyJoinKeys, UnsetType] = unset,
        step_aliases: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        User journey search configuration.

        :param expression: Expression string.
        :type expression: str

        :param filters: Filters for user journey search.
        :type filters: UserJourneySearchFilters, optional

        :param join_keys: Join keys for user journey queries.
        :type join_keys: UserJourneyJoinKeys, optional

        :param node_objects: Node objects mapping.
        :type node_objects: {str: (ProductAnalyticsBaseQuery,)}

        :param step_aliases: Step aliases mapping.
        :type step_aliases: {str: (str,)}, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        if step_aliases is not unset:
            kwargs["step_aliases"] = step_aliases
        super().__init__(kwargs)

        self_.expression = expression
        self_.node_objects = node_objects
