# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.events_aggregation import EventsAggregation


class SankeyNetworkQueryCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.events_aggregation import EventsAggregation

        return {
            "aggregation": (EventsAggregation,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(self_, aggregation: Union[EventsAggregation, str, str], metric: str, **kwargs):
        """
        Compute aggregation for network queries.

        :param aggregation: The type of aggregation that can be performed on events-based queries.
        :type aggregation: EventsAggregation

        :param metric: Metric to aggregate.
        :type metric: str
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.metric = metric
