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
    from datadog_api_client.v1.model.user_journey_formula_compute import UserJourneyFormulaCompute
    from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
    from datadog_api_client.v1.model.user_journey_formula_group_by import UserJourneyFormulaGroupBy
    from datadog_api_client.v1.model.user_journey_search import UserJourneySearch


class FormulaAndFunctionUserJourneyQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.user_journey_formula_compute import UserJourneyFormulaCompute
        from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
        from datadog_api_client.v1.model.user_journey_formula_group_by import UserJourneyFormulaGroupBy
        from datadog_api_client.v1.model.user_journey_search import UserJourneySearch

        return {
            "compute": (UserJourneyFormulaCompute,),
            "data_source": (ProductAnalyticsFunnelDataSource,),
            "group_by": ([UserJourneyFormulaGroupBy],),
            "name": (str,),
            "search": (UserJourneySearch,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
    }

    def __init__(
        self_,
        compute: UserJourneyFormulaCompute,
        data_source: ProductAnalyticsFunnelDataSource,
        name: str,
        search: UserJourneySearch,
        group_by: Union[List[UserJourneyFormulaGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions User Journey query for defining funnel, timeseries, and scalar visualizations over journey data.

        :param compute: Compute configuration for User Journey formula queries.
        :type compute: UserJourneyFormulaCompute

        :param data_source: Data source for user journey funnel queries.
        :type data_source: ProductAnalyticsFunnelDataSource

        :param group_by: Group by configuration.
        :type group_by: [UserJourneyFormulaGroupBy], optional

        :param name: Name of the query for use in formulas.
        :type name: str

        :param search: User journey search configuration.
        :type search: UserJourneySearch
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.search = search
