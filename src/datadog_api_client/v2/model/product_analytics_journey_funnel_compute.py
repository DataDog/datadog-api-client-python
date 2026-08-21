# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsJourneyFunnelCompute(ModelNormal):
    validations = {
        "aggregation": {},
    }

    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(self_, aggregation: Union[str, UnsetType] = unset, metric: Union[str, UnsetType] = unset, **kwargs):
        """
        Defines the metric computed at each funnel step.

        :param aggregation: Aggregation function: ``count`` , ``cardinality`` , ``avg`` , ``median`` , ``min`` , ``max`` , ``sum`` ,
            or a percentile of the form ``pc<N>`` such as ``pc95``. Defaults to ``cardinality``.
        :type aggregation: str, optional

        :param metric: Metric to aggregate on. Defaults to the identity join key.
        :type metric: str, optional
        """
        if aggregation is not unset:
            kwargs["aggregation"] = aggregation
        if metric is not unset:
            kwargs["metric"] = metric
        super().__init__(kwargs)
