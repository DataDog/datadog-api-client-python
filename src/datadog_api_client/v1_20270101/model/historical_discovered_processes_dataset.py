# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.historical_discovered_processes_dataset_data_source import (
        HistoricalDiscoveredProcessesDatasetDataSource,
    )


class HistoricalDiscoveredProcessesDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.historical_discovered_processes_dataset_data_source import (
            HistoricalDiscoveredProcessesDatasetDataSource,
        )

        return {
            "data_source": (HistoricalDiscoveredProcessesDatasetDataSource,),
            "name": (str,),
            "timestamp": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "timestamp": "timestamp",
    }

    def __init__(
        self_, data_source: HistoricalDiscoveredProcessesDatasetDataSource, name: str, timestamp: str, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: HistoricalDiscoveredProcessesDatasetDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param timestamp: Test-only generated schema for the dashboard versioning proof of concept.
        :type timestamp: str
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.timestamp = timestamp
