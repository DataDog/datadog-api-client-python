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
    from datadog_api_client.v1_20270101.model.list_column import ListColumn
    from datadog_api_client.v1_20270101.model.composite_referential_data_query_compute_items import (
        CompositeReferentialDataQueryComputeItems,
    )
    from datadog_api_client.v1_20270101.model.composite_referential_data_query_data_source import (
        CompositeReferentialDataQueryDataSource,
    )


class CompositeReferentialDataQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.list_column import ListColumn
        from datadog_api_client.v1_20270101.model.composite_referential_data_query_compute_items import (
            CompositeReferentialDataQueryComputeItems,
        )
        from datadog_api_client.v1_20270101.model.composite_referential_data_query_data_source import (
            CompositeReferentialDataQueryDataSource,
        )

        return {
            "columns": ([ListColumn],),
            "compute": ([CompositeReferentialDataQueryComputeItems],),
            "data_source": (CompositeReferentialDataQueryDataSource,),
            "group_by": ([str],),
            "name": (str,),
            "query_filter": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "query_filter": "query_filter",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        data_source: CompositeReferentialDataQueryDataSource,
        name: str,
        table_name: str,
        columns: Union[List[ListColumn], UnsetType] = unset,
        compute: Union[List[CompositeReferentialDataQueryComputeItems], UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ListColumn], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [CompositeReferentialDataQueryComputeItems], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: CompositeReferentialDataQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.table_name = table_name
