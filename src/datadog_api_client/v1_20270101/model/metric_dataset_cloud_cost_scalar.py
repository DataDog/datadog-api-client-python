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
    from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar_aggregation import (
        MetricDatasetCloudCostScalarAggregation,
    )
    from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar_data_source import (
        MetricDatasetCloudCostScalarDataSource,
    )
    from datadog_api_client.v1_20270101.model.time_window import TimeWindow


class MetricDatasetCloudCostScalar(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar_aggregation import (
            MetricDatasetCloudCostScalarAggregation,
        )
        from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar_data_source import (
            MetricDatasetCloudCostScalarDataSource,
        )
        from datadog_api_client.v1_20270101.model.time_window import TimeWindow

        return {
            "aggregation": (MetricDatasetCloudCostScalarAggregation,),
            "data_source": (MetricDatasetCloudCostScalarDataSource,),
            "metric_name": (str,),
            "name": (str,),
            "query_filter": (str,),
            "tag_names": ([str],),
            "time_window": (TimeWindow,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "data_source": "data_source",
        "metric_name": "metric_name",
        "name": "name",
        "query_filter": "query_filter",
        "tag_names": "tag_names",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        aggregation: MetricDatasetCloudCostScalarAggregation,
        data_source: MetricDatasetCloudCostScalarDataSource,
        metric_name: str,
        name: str,
        query_filter: Union[str, UnsetType] = unset,
        tag_names: Union[List[str], UnsetType] = unset,
        time_window: Union[TimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: MetricDatasetCloudCostScalarAggregation

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: MetricDatasetCloudCostScalarDataSource

        :param metric_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric_name: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param tag_names: Test-only generated schema for the dashboard versioning proof of concept.
        :type tag_names: [str], optional

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional
        """
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if tag_names is not unset:
            kwargs["tag_names"] = tag_names
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.data_source = data_source
        self_.metric_name = metric_name
        self_.name = name
