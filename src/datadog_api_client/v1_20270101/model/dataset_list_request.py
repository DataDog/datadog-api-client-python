# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dataset_list_request_columns_items import DatasetListRequestColumnsItems
    from datadog_api_client.v1_20270101.model.dataset_list_request20270101_query import DatasetListRequest20270101Query
    from datadog_api_client.v1_20270101.model.dataset_list_request_request_type import DatasetListRequestRequestType
    from datadog_api_client.v1_20270101.model.dataset_list_query import DatasetListQuery
    from datadog_api_client.v1_20270101.model.relational_data_query import RelationalDataQuery


class DatasetListRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_list_request_columns_items import (
            DatasetListRequestColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.dataset_list_request20270101_query import (
            DatasetListRequest20270101Query,
        )
        from datadog_api_client.v1_20270101.model.dataset_list_request_request_type import DatasetListRequestRequestType

        return {
            "columns": ([DatasetListRequestColumnsItems],),
            "query": (DatasetListRequest20270101Query,),
            "request_type": (DatasetListRequestRequestType,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        columns: List[DatasetListRequestColumnsItems],
        query: Union[DatasetListRequest20270101Query, DatasetListQuery, RelationalDataQuery],
        request_type: DatasetListRequestRequestType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetListRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: DatasetListRequest20270101Query

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: DatasetListRequestRequestType
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.request_type = request_type
