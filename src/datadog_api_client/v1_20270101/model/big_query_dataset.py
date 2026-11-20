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
    from datadog_api_client.v1_20270101.model.big_query_dataset_data_source import BigQueryDatasetDataSource


class BigQueryDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.big_query_dataset_data_source import BigQueryDatasetDataSource

        return {
            "data_source": (BigQueryDatasetDataSource,),
            "name": (str,),
            "sql_query": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "sql_query": "sql_query",
    }

    def __init__(self_, data_source: BigQueryDatasetDataSource, name: str, sql_query: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: BigQueryDatasetDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param sql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type sql_query: str
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.sql_query = sql_query
