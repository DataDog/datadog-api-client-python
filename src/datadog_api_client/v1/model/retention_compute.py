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
    from datadog_api_client.v1.model.retention_compute_metric import RetentionComputeMetric


class RetentionCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.events_aggregation import EventsAggregation
        from datadog_api_client.v1.model.retention_compute_metric import RetentionComputeMetric

        return {
            "aggregation": (EventsAggregation,),
            "metric": (RetentionComputeMetric,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(self_, aggregation: Union[EventsAggregation, str, str], metric: RetentionComputeMetric, **kwargs):
        """
        Compute configuration for retention queries.

        :param aggregation: The type of aggregation that can be performed on events-based queries.
        :type aggregation: EventsAggregation

        :param metric: Metric for retention compute.
        :type metric: RetentionComputeMetric
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.metric = metric
