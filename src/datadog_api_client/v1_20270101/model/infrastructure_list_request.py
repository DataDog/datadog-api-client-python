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
    from datadog_api_client.v1_20270101.model.infrastructure_list_request_columns_items import (
        InfrastructureListRequestColumnsItems,
    )
    from datadog_api_client.v1_20270101.model.infrastructure_list_query import InfrastructureListQuery
    from datadog_api_client.v1_20270101.model.infrastructure_list_request_request_type import (
        InfrastructureListRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class InfrastructureListRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.infrastructure_list_request_columns_items import (
            InfrastructureListRequestColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.infrastructure_list_query import InfrastructureListQuery
        from datadog_api_client.v1_20270101.model.infrastructure_list_request_request_type import (
            InfrastructureListRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort

        return {
            "columns": ([InfrastructureListRequestColumnsItems],),
            "query": (InfrastructureListQuery,),
            "request_type": (InfrastructureListRequestRequestType,),
            "sort": (ListStreamSort,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "request_type": "request_type",
        "sort": "sort",
    }

    def __init__(
        self_,
        columns: List[InfrastructureListRequestColumnsItems],
        query: InfrastructureListQuery,
        request_type: InfrastructureListRequestRequestType,
        sort: Union[ListStreamSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [InfrastructureListRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: InfrastructureListQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: InfrastructureListRequestRequestType

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ListStreamSort, optional
        """
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.request_type = request_type
