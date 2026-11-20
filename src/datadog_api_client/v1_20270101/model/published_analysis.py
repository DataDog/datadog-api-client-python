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
    from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
    from datadog_api_client.v1_20270101.model.published_analysis_data_source import PublishedAnalysisDataSource
    from datadog_api_client.v1_20270101.model.time_window import TimeWindow


class PublishedAnalysis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
        from datadog_api_client.v1_20270101.model.published_analysis_data_source import PublishedAnalysisDataSource
        from datadog_api_client.v1_20270101.model.time_window import TimeWindow

        return {
            "columns": ([DatasetColumn],),
            "data_source": (PublishedAnalysisDataSource,),
            "dataset_id": (str,),
            "name": (str,),
            "query_filter": (str,),
            "time_window": (TimeWindow,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "dataset_id": "dataset_id",
        "name": "name",
        "query_filter": "query_filter",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        data_source: PublishedAnalysisDataSource,
        dataset_id: str,
        name: str,
        columns: Union[List[DatasetColumn], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        time_window: Union[TimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetColumn], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: PublishedAnalysisDataSource

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.dataset_id = dataset_id
        self_.name = name
