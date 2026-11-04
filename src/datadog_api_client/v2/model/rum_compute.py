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
    from datadog_api_client.v2.model.rum_aggregation_function import RUMAggregationFunction
    from datadog_api_client.v2.model.rum_compute_type import RUMComputeType


class RUMCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_aggregation_function import RUMAggregationFunction
        from datadog_api_client.v2.model.rum_compute_type import RUMComputeType

        return {
            "aggregation": (RUMAggregationFunction,),
            "interval": (str,),
            "metric": (str,),
            "type": (RUMComputeType,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "type": "type",
    }

    def __init__(
        self_,
        aggregation: RUMAggregationFunction,
        interval: Union[str, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        type: Union[RUMComputeType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A compute rule to compute metrics or timeseries. In the response, the result of each rule is keyed ``c0`` , ``c1``... following the order of the ``compute`` list.

        :param aggregation: An aggregation function. ``count`` counts events and needs no metric. ``cardinality`` counts the distinct values of the metric. ``sum`` , ``min`` , ``max`` , ``avg`` , ``median`` and the percentiles ( ``pc75`` to ``pc99`` ) apply to a numeric metric such as ``@view.loading_time``.
        :type aggregation: RUMAggregationFunction

        :param interval: The time buckets' size, for example ``5m`` , ``1h`` or ``1d`` (only used for ``type=timeseries`` ).
            Defaults to a resolution of 150 points over the queried time range.
        :type interval: str, optional

        :param metric: The attribute to aggregate, for example ``@view.loading_time``. Not needed for ``count`` , required for the other aggregations.
        :type metric: str, optional

        :param type: The type of compute. ``total`` returns one value per bucket, ``timeseries`` returns a list of time points per bucket.
        :type type: RUMComputeType, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.aggregation = aggregation
