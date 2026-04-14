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
    from datadog_api_client.v1.model.calendar_interval import CalendarInterval


class ProductAnalyticsExtendedCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_event_aggregation import (
            FormulaAndFunctionEventAggregation,
        )
        from datadog_api_client.v1.model.calendar_interval import CalendarInterval

        return {
            "aggregation": (FormulaAndFunctionEventAggregation,),
            "interval": (float,),
            "metric": (str,),
            "name": (str,),
            "rollup": (CalendarInterval,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "name": "name",
        "rollup": "rollup",
    }

    def __init__(
        self_,
        aggregation: FormulaAndFunctionEventAggregation,
        interval: Union[float, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rollup: Union[CalendarInterval, UnsetType] = unset,
        **kwargs,
    ):
        """
        Compute configuration for Product Analytics Extended queries.

        :param aggregation: Aggregation methods for event platform queries.
        :type aggregation: FormulaAndFunctionEventAggregation

        :param interval: Fixed-width time bucket interval in milliseconds for time series queries. Mutually exclusive with ``rollup``.
        :type interval: float, optional

        :param metric: Measurable attribute to compute.
        :type metric: str, optional

        :param name: Name of the compute for use in formulas.
        :type name: str, optional

        :param rollup: Calendar interval definition.
        :type rollup: CalendarInterval, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if name is not unset:
            kwargs["name"] = name
        if rollup is not unset:
            kwargs["rollup"] = rollup
        super().__init__(kwargs)

        self_.aggregation = aggregation
