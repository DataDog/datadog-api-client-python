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
    from datadog_api_client.v1_20270101.model.dataset_compute20270101_aggregation import (
        DatasetCompute20270101Aggregation,
    )
    from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator


class DatasetCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_compute20270101_aggregation import (
            DatasetCompute20270101Aggregation,
        )

        return {
            "aggregation": (DatasetCompute20270101Aggregation,),
            "column": (str,),
            "interval": (float,),
            "name": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "column": "column",
        "interval": "interval",
        "name": "name",
    }

    def __init__(
        self_,
        aggregation: Union[DatasetCompute20270101Aggregation, str, EventsAggregator],
        name: str,
        column: Union[str, UnsetType] = unset,
        interval: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: DatasetCompute20270101Aggregation

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str, optional

        :param interval: Test-only generated schema for the dashboard versioning proof of concept.
        :type interval: float, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if column is not unset:
            kwargs["column"] = column
        if interval is not unset:
            kwargs["interval"] = interval
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.name = name
