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
    from datadog_api_client.v1_20270101.model.case_compute import CaseCompute
    from datadog_api_client.v1_20270101.model.formula_case_query_data_source import FormulaCaseQueryDataSource
    from datadog_api_client.v1_20270101.model.case_group_by import CaseGroupBy
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class FormulaCaseQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.case_compute import CaseCompute
        from datadog_api_client.v1_20270101.model.formula_case_query_data_source import FormulaCaseQueryDataSource
        from datadog_api_client.v1_20270101.model.case_group_by import CaseGroupBy
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "compute": (CaseCompute,),
            "data_source": (FormulaCaseQueryDataSource,),
            "group_by": ([CaseGroupBy],),
            "limit": (float,),
            "name": (str,),
            "query_filter": (str,),
            "sort": (QuerySortOrder,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "limit": "limit",
        "name": "name",
        "query_filter": "query_filter",
        "sort": "sort",
    }

    def __init__(
        self_,
        compute: CaseCompute,
        data_source: FormulaCaseQueryDataSource,
        name: str,
        query_filter: str,
        group_by: Union[List[CaseGroupBy], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        sort: Union[QuerySortOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: CaseCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaCaseQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [CaseGroupBy], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: QuerySortOrder, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.query_filter = query_filter
