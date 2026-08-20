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
    from datadog_api_client.v2.model.product_analytics_formula_journey_query import ProductAnalyticsFormulaJourneyQuery


class ProductAnalyticsFormulaJourneyRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_formula_journey_query import (
            ProductAnalyticsFormulaJourneyQuery,
        )

        return {
            "_from": (int,),
            "interval": (int,),
            "query": (ProductAnalyticsFormulaJourneyQuery,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "interval": "interval",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_,
        _from: int,
        query: ProductAnalyticsFormulaJourneyQuery,
        to: int,
        interval: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a journey timeseries request.

        :param _from: Start of the query window, in epoch milliseconds.
        :type _from: int

        :param interval: Time bucket interval in milliseconds.
        :type interval: int, optional

        :param query: Query definition for a journey timeseries request.
        :type query: ProductAnalyticsFormulaJourneyQuery

        :param to: End of the query window, in epoch milliseconds.
        :type to: int
        """
        if interval is not unset:
            kwargs["interval"] = interval
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
