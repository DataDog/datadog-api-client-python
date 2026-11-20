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
    from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
    from datadog_api_client.v1_20270101.model.case_metric import CaseMetric


class CaseCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
        from datadog_api_client.v1_20270101.model.case_metric import CaseMetric

        return {
            "aggregation": (EventsAggregator,),
            "metric": (CaseMetric,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(
        self_, aggregation: Union[EventsAggregator, str], metric: Union[CaseMetric, UnsetType] = unset, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: EventsAggregator

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: CaseMetric, optional
        """
        if metric is not unset:
            kwargs["metric"] = metric
        super().__init__(kwargs)

        self_.aggregation = aggregation
