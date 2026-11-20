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
    from datadog_api_client.v1_20270101.model.analysis_dataset_data_source import AnalysisDatasetDataSource
    from datadog_api_client.v1_20270101.model.analysis_dataset20270101_query import AnalysisDataset20270101Query
    from datadog_api_client.v1_20270101.model.sql_analysis_query import SqlAnalysisQuery
    from datadog_api_client.v1_20270101.model.structured_analysis_query import StructuredAnalysisQuery
    from datadog_api_client.v1_20270101.model.sampled_analysis_query import SampledAnalysisQuery


class AnalysisDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.analysis_dataset_data_source import AnalysisDatasetDataSource
        from datadog_api_client.v1_20270101.model.analysis_dataset20270101_query import AnalysisDataset20270101Query

        return {
            "data_source": (AnalysisDatasetDataSource,),
            "name": (str,),
            "query": (AnalysisDataset20270101Query,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        data_source: AnalysisDatasetDataSource,
        name: str,
        query: Union[AnalysisDataset20270101Query, SqlAnalysisQuery, StructuredAnalysisQuery, SampledAnalysisQuery],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AnalysisDatasetDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: AnalysisDataset20270101Query
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
