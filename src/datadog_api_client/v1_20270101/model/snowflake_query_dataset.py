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
    from datadog_api_client.v1_20270101.model.snowflake_query_dataset_data_source import SnowflakeQueryDatasetDataSource


class SnowflakeQueryDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.snowflake_query_dataset_data_source import (
            SnowflakeQueryDatasetDataSource,
        )

        return {
            "data_source": (SnowflakeQueryDatasetDataSource,),
            "name": (str,),
            "sql_query": (str,),
            "warehouse": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "sql_query": "sql_query",
        "warehouse": "warehouse",
    }

    def __init__(
        self_,
        data_source: SnowflakeQueryDatasetDataSource,
        name: str,
        sql_query: str,
        warehouse: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: SnowflakeQueryDatasetDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param sql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type sql_query: str

        :param warehouse: Test-only generated schema for the dashboard versioning proof of concept.
        :type warehouse: str, optional
        """
        if warehouse is not unset:
            kwargs["warehouse"] = warehouse
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.sql_query = sql_query
