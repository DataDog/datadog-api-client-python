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
    from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation
    from datadog_api_client.v1.model.user_journey_formula_compute_metric import UserJourneyFormulaComputeMetric
    from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget


class UserJourneyFormulaCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_event_aggregation import (
            FormulaAndFunctionEventAggregation,
        )
        from datadog_api_client.v1.model.user_journey_formula_compute_metric import UserJourneyFormulaComputeMetric
        from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget

        return {
            "aggregation": (FormulaAndFunctionEventAggregation,),
            "interval": (float,),
            "metric": (UserJourneyFormulaComputeMetric,),
            "target": (UserJourneySearchTarget,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "target": "target",
    }

    def __init__(
        self_,
        aggregation: FormulaAndFunctionEventAggregation,
        interval: Union[float, UnsetType] = unset,
        metric: Union[UserJourneyFormulaComputeMetric, UnsetType] = unset,
        target: Union[UserJourneySearchTarget, UnsetType] = unset,
        **kwargs,
    ):
        """
        Compute configuration for User Journey formula queries.

        :param aggregation: Aggregation methods for event platform queries.
        :type aggregation: FormulaAndFunctionEventAggregation

        :param interval: Time bucket interval in milliseconds for time series queries.
        :type interval: float, optional

        :param metric: Metric for User Journey formula compute. ``__dd.conversion`` and ``__dd.conversion_rate`` accept ``count`` and ``cardinality`` as aggregations. ``__dd.time_to_convert`` accepts ``avg`` , ``median`` , ``pc75`` , ``pc95`` , ``pc98`` , ``pc99`` , ``min`` , and ``max``.
        :type metric: UserJourneyFormulaComputeMetric, optional

        :param target: Target for user journey search.
        :type target: UserJourneySearchTarget, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.aggregation = aggregation
